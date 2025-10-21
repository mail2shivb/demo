import os
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from dotenv import load_dotenv

load_dotenv()

COSMOS_URL = os.environ.get("COSMOS_URL")
COSMOS_KEY = os.environ.get("COSMOS_KEY")
COSMOS_DB = os.environ.get("COSMOS_DB", "company_ref_db")
COSMOS_CONTAINER = os.environ.get("COSMOS_CONTAINER", "companies")
COSMOS_AUTOSCALE_MAX_RU = int(os.environ.get("COSMOS_AUTOSCALE_MAX_RU", "4000"))

# Lazy initialization of client
_client = None

def get_client():
    global _client
    if _client is None:
        # Check if we have valid credentials before initializing client
        if not COSMOS_URL or not COSMOS_KEY or COSMOS_URL == "https://<your-account>.documents.azure.com:443/" or COSMOS_KEY == "<primary-or-secondary-key>":
            raise RuntimeError("Azure Cosmos DB credentials not configured. Please update .env file with valid COSMOS_URL and COSMOS_KEY")
        _client = CosmosClient(COSMOS_URL, credential=COSMOS_KEY)
    return _client

def get_container():
    client = get_client()
    
    try:
        database = client.create_database_if_not_exists(id=COSMOS_DB)
    except exceptions.CosmosResourceExistsError:
        database = client.get_database_client(COSMOS_DB)

    unique_key_policy = {
        "uniqueKeys": [
            {"paths": ["/name_lower"]},
            {"paths": ["/lei"]},
            {"paths": ["/ticker"]},
        ]
    }

    try:
        container = database.create_container_if_not_exists(
            id=COSMOS_CONTAINER,
            partition_key=PartitionKey(path="/pk"),
            offer_throughput=None,
            autoscale_throughput=COSMOS_AUTOSCALE_MAX_RU,
            unique_key_policy=unique_key_policy,
            indexing_policy={
                "indexingMode": "consistent",
                "automatic": True,
                "includedPaths": [{"path": "/*"}],
                "excludedPaths": [
                    {"path": "/\"_etag\"/?"},
                    {"path": "/notes/?"}
                ]
            },
        )
    except exceptions.CosmosResourceExistsError:
        container = database.get_container_client(COSMOS_CONTAINER)

    return container
