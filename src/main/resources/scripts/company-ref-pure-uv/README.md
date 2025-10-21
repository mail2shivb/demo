# Company Reference API (FastAPI + Azure Cosmos DB)

Reference data service for Corporate Takeover analysis.

## Features
- CRUD for companies with takeover-relevant fields (anti-takeover, shareholders, identifiers)
- Validate-by-name: `/companies/validate?name=...`
- Search by name prefix: `/companies/search?prefix=...`
- Unique keys on normalized name, LEI, and ticker
- Cosmos DB (NoSQL) with autoscale, indexing policy, partition key

## Local Run (pure uv)

```bash
# install uv once (choose one)
pipx install uv    # recommended
# or: pip install uv

uv sync --in-project
uv run uvicorn app.main:app --port 8000 --reload
```

Open http://localhost:8000/docs

## Legacy pip (optional)
If you must use pip, export requirements from the lock (not recommended):
```bash
uv export -o requirements.txt
pip install -r requirements.txt
```


```bash
python -m venv .venv && source .venv/bin/activate
cp .env.example .env  # then edit values
uvicorn app.main:app --port 8000 --reload
```

Open http://localhost:8000/docs

## Deploy to Azure App Service (GitHub Actions)

1. **Create Azure resources** (example names):
   - Resource Group
   - Azure Cosmos DB (NoSQL) account + DB + Container (the app can create DB/Container on first run)
   - App Service Plan (Linux) + Web App (Python 3.12)
2. **App Settings** on the Web App (Configuration → Application settings):
   - `COSMOS_URL`, `COSMOS_KEY`, `COSMOS_DB`, `COSMOS_CONTAINER`, `COSMOS_AUTOSCALE_MAX_RU` (optional)
3. **GitHub Secrets** in your repository:
   - `AZURE_CREDENTIALS` → JSON of an Azure Service Principal with access to the Web App.
     Example JSON:
     ```json
     {
       "clientId": "xxxxx-xxxx-xxxx-xxxx",
       "clientSecret": "********",
       "subscriptionId": "xxxxx-xxxx-xxxx-xxxx",
       "tenantId": "xxxxx-xxxx-xxxx-xxxx",
       "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
       "resourceManagerEndpointUrl": "https://management.azure.com/",
       "activeDirectoryGraphResourceId": "https://graph.windows.net/",
       "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
       "galleryEndpointUrl": "https://gallery.azure.com/",
       "managementEndpointUrl": "https://management.core.windows.net/"
     }
     ```
   - `AZURE_WEBAPP_NAME` → your Web App name (e.g., `company-ref-api`)
   - `AZURE_RG` → resource group name (optional if using publish profile instead)
   - Alternatively, use `AZURE_WEBAPP_PUBLISH_PROFILE` secret (publish profile XML).

4. **Push to `main`** and the workflow will build and deploy.

## Startup command (Azure App Service → Configuration → General settings)
Use:
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## Endpoints
- `POST /companies` — create
- `GET /companies/{pk}/{id}` — read
- `PUT /companies/{pk}/{id}` — update
- `DELETE /companies/{pk}/{id}` — delete
- `GET /companies/search?prefix=...&limit=20`
- `GET /companies/validate?name=...`
- `GET /companies/lookup?ticker=...&isin=...&lei=...`
- `GET /health`

## Notes
- Partition key is `/pk`, derived from the first letter of the normalized company name.
- To switch to LEI as partition key, adjust `get_container()` in `app/db.py`.
