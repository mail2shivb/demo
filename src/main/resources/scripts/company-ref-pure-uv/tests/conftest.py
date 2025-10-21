"""
Test utilities and fixtures for the Company Reference API tests.
"""
import pytest
from unittest.mock import Mock, MagicMock, patch
from typing import Dict, Any, List, Optional
from fastapi.testclient import TestClient


class MockCosmosContainer:
    """Mock Azure Cosmos DB container for testing."""
    
    def __init__(self):
        self.items: List[Dict[str, Any]] = []
        self.next_id = 1
    
    def create_item(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Mock create_item method."""
        item = body.copy()
        if "id" not in item:
            item["id"] = str(self.next_id)
            self.next_id += 1
        
        # Check for unique key violations (simplified)
        for existing in self.items:
            if existing.get("name_lower") == item.get("name_lower"):
                from azure.cosmos.exceptions import CosmosHttpResponseError
                raise CosmosHttpResponseError(status_code=409, message="Conflict")
            if item.get("lei") and existing.get("lei") == item.get("lei"):
                from azure.cosmos.exceptions import CosmosHttpResponseError
                raise CosmosHttpResponseError(status_code=409, message="Conflict")
            if item.get("ticker") and existing.get("ticker") == item.get("ticker"):
                from azure.cosmos.exceptions import CosmosHttpResponseError
                raise CosmosHttpResponseError(status_code=409, message="Conflict")
        
        self.items.append(item)
        return item
    
    def read_item(self, item: str, partition_key: str) -> Dict[str, Any]:
        """Mock read_item method."""
        for existing in self.items:
            if existing["id"] == item and existing["pk"] == partition_key:
                return existing
        from azure.cosmos.exceptions import CosmosResourceNotFoundError
        raise CosmosResourceNotFoundError()
    
    def replace_item(self, item: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """Mock replace_item method."""
        for i, existing in enumerate(self.items):
            if existing["id"] == item:
                self.items[i] = body
                return body
        from azure.cosmos.exceptions import CosmosResourceNotFoundError
        raise CosmosResourceNotFoundError()
        from azure.cosmos.exceptions import CosmosResourceNotFoundError
        raise CosmosResourceNotFoundError()
    
    def delete_item(self, item: str, partition_key: str):
        """Mock delete_item method."""
        for i, existing in enumerate(self.items):
            if existing["id"] == item and existing["pk"] == partition_key:
                del self.items[i]
                return
        from azure.cosmos.exceptions import CosmosResourceNotFoundError
        raise CosmosResourceNotFoundError()
    
    def query_items(self, query: str, parameters: List[Dict[str, Any]], 
                   enable_cross_partition_query: bool = False) -> List[Dict[str, Any]]:
        """Mock query_items method (simplified query processing)."""
        # Extract parameter values
        param_dict = {}
        for param in parameters:
            param_dict[param["name"]] = param["value"]
        
        results = []
        
        # Handle different query types (simplified)
        if "WHERE c.name_lower = @nl" in query:
            nl = param_dict.get("@nl")
            results = [item for item in self.items if item.get("name_lower") == nl]
        
        elif "WHERE STARTSWITH(c.name_lower, @p)" in query:
            p = param_dict.get("@p")
            limit = param_dict.get("@lim", 20)
            results = [item for item in self.items if item.get("name_lower", "").startswith(p)]
            results = sorted(results, key=lambda x: x.get("name_lower", ""))[:limit]
        
        elif "c.ticker" in query or "c.isin" in query or "c.lei" in query:
            # Handle key lookups (both single criteria and OR combinations)
            ticker = param_dict.get("@t")
            isin = param_dict.get("@i")
            lei = param_dict.get("@l")
            
            for item in self.items:
                match = False
                if ticker and item.get("ticker") == ticker:
                    match = True
                if isin and item.get("isin") == isin:
                    match = True
                if lei and item.get("lei") == lei:
                    match = True
                
                if match and item not in results:
                    results.append(item)
        
        return results


@pytest.fixture
def mock_container():
    """Provide a mock Cosmos DB container."""
    return MockCosmosContainer()


@pytest.fixture
def sample_company_data():
    """Provide sample company data for testing."""
    return {
        "name": "Apple Inc.",
        "ticker": "AAPL",
        "isin": "US0378331005",
        "lei": "HWUPKR0MPOU8FGXBT394",
        "country": "US",
        "sector": "Technology",
        "anti_takeover_provisions": ["poison_pill", "staggered_board"],
        "major_shareholders": [
            {"name": "Vanguard Group", "percentage": 7.5},
            {"name": "BlackRock", "percentage": 6.8}
        ],
        "notes": "Leading technology company"
    }


@pytest.fixture
def sample_companies_list():
    """Provide a list of sample companies for testing."""
    return [
        {
            "name": "Apple Inc.",
            "ticker": "AAPL",
            "isin": "US0378331005",
            "lei": "HWUPKR0MPOU8FGXBT394",
            "country": "US",
            "sector": "Technology"
        },
        {
            "name": "Microsoft Corporation",
            "ticker": "MSFT", 
            "isin": "US5949181045",
            "lei": "XKZZ2JZF41MRHTR1V493",
            "country": "US",
            "sector": "Technology"
        },
        {
            "name": "Amazon.com Inc.",
            "ticker": "AMZN",
            "isin": "US0231351067",
            "lei": "PQOH26KWDF7CG10L6792",
            "country": "US",
            "sector": "Consumer Discretionary"
        }
    ]


def create_test_client():
    """Create a FastAPI test client with mocked database."""
    from app.main import app
    return TestClient(app)


@pytest.fixture
def test_client():
    """Provide a FastAPI test client."""
    return create_test_client()


@pytest.fixture
def mock_get_container(mock_container):
    """Mock the get_container function to return our mock container."""
    with patch('app.db.get_container', return_value=mock_container):
        with patch('app.repository.company_repository.get_container', return_value=mock_container):
            yield mock_container


@pytest.fixture
def mock_company_repository(mock_container):
    """Provide a mocked CompanyRepository."""
    from app.repository.company_repository import CompanyRepository
    repo = CompanyRepository()
    repo._container = mock_container
    return repo


@pytest.fixture
def mock_company_service(mock_company_repository):
    """Provide a mocked CompanyService."""
    from app.services.company_service import CompanyService
    service = CompanyService()
    service.repository = mock_company_repository
    return service