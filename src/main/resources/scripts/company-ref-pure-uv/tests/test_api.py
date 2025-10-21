"""
Integration tests for the FastAPI endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app


class TestHealthEndpoint:
    """Test the health endpoint."""
    
    def test_health_endpoint_without_db_config(self):
        """Test health endpoint when database is not configured."""
        client = TestClient(app)
        
        response = client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "ok"
        assert data["database"] == "not_configured"
        assert "message" in data


class TestCompanyEndpoints:
    """Test the company CRUD endpoints."""
    
    @pytest.fixture
    def client_with_mock_db(self, mock_get_container):
        """Create test client with mocked database."""
        client = TestClient(app)
        return client
    
    def test_create_company_success(self, client_with_mock_db, sample_company_data):
        """Test successfully creating a company."""
        client = client_with_mock_db
        
        # Prepare request data (remove fields not in create model)
        create_data = {
            "name": sample_company_data["name"],
            "ticker": sample_company_data["ticker"],
            "isin": sample_company_data["isin"],
            "lei": sample_company_data["lei"],
            "country": sample_company_data["country"],
            "sector": sample_company_data["sector"],
            "notes": sample_company_data["notes"]
        }
        
        response = client.post("/companies", json=create_data)
        assert response.status_code == 201
        
        data = response.json()
        assert data["name"] == sample_company_data["name"]
        assert data["ticker"] == sample_company_data["ticker"]
        assert "id" in data
        assert "pk" in data
        assert "name_lower" in data
    
    def test_create_company_missing_name(self, client_with_mock_db):
        """Test creating company without required name field."""
        client = client_with_mock_db
        
        response = client.post("/companies", json={"ticker": "AAPL"})
        assert response.status_code == 422
    
    def test_create_company_duplicate_name(self, client_with_mock_db, sample_company_data):
        """Test creating company with duplicate name."""
        client = client_with_mock_db
        
        create_data = {
            "name": sample_company_data["name"],
            "ticker": sample_company_data["ticker"]
        }
        
        # Create first company
        response1 = client.post("/companies", json=create_data)
        assert response1.status_code == 201
        
        # Try to create duplicate
        response2 = client.post("/companies", json=create_data)
        assert response2.status_code == 409 or response2.status_code == 400
    
    def test_get_company_success(self, client_with_mock_db, sample_company_data):
        """Test successfully retrieving a company."""
        client = client_with_mock_db
        
        # Create company first
        create_data = {
            "name": sample_company_data["name"],
            "ticker": sample_company_data["ticker"]
        }
        create_response = client.post("/companies", json=create_data)
        created = create_response.json()
        
        # Get the company
        response = client.get(f"/companies/{created['pk']}/{created['id']}")
        assert response.status_code == 200
        
        data = response.json()
        assert data["id"] == created["id"]
        assert data["name"] == sample_company_data["name"]
    
    def test_get_company_not_found(self, client_with_mock_db):
        """Test retrieving non-existent company."""
        client = client_with_mock_db
        
        response = client.get("/companies/n/nonexistent")
        assert response.status_code == 404
    
    def test_update_company_success(self, client_with_mock_db, sample_company_data):
        """Test successfully updating a company."""
        client = client_with_mock_db
        
        # Create company first
        create_data = {
            "name": sample_company_data["name"],
            "ticker": sample_company_data["ticker"]
        }
        create_response = client.post("/companies", json=create_data)
        created = create_response.json()
        
        # Update the company
        update_data = {
            "sector": "Consumer Electronics",
            "notes": "Updated notes"
        }
        response = client.put(f"/companies/{created['pk']}/{created['id']}", json=update_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["sector"] == "Consumer Electronics"
        assert data["notes"] == "Updated notes"
        assert data["name"] == sample_company_data["name"]  # Unchanged
    
    def test_update_company_not_found(self, client_with_mock_db):
        """Test updating non-existent company."""
        client = client_with_mock_db
        
        update_data = {"sector": "Technology"}
        response = client.put("/companies/n/nonexistent", json=update_data)
        assert response.status_code == 404
    
    def test_delete_company_success(self, client_with_mock_db, sample_company_data):
        """Test successfully deleting a company."""
        client = client_with_mock_db
        
        # Create company first
        create_data = {
            "name": sample_company_data["name"],
            "ticker": sample_company_data["ticker"]
        }
        create_response = client.post("/companies", json=create_data)
        created = create_response.json()
        
        # Delete the company
        response = client.delete(f"/companies/{created['pk']}/{created['id']}")
        assert response.status_code == 204
        
        # Verify company is deleted
        get_response = client.get(f"/companies/{created['pk']}/{created['id']}")
        assert get_response.status_code == 404
    
    def test_delete_company_not_found(self, client_with_mock_db):
        """Test deleting non-existent company."""
        client = client_with_mock_db
        
        response = client.delete("/companies/n/nonexistent")
        assert response.status_code == 404


class TestSearchEndpoints:
    """Test the search and lookup endpoints."""
    
    @pytest.fixture
    def client_with_test_data(self, mock_get_container, sample_companies_list):
        """Create test client with sample data."""
        client = TestClient(app)
        
        # Add sample companies
        for company_data in sample_companies_list:
            create_data = {
                "name": company_data["name"],
                "ticker": company_data["ticker"],
                "isin": company_data.get("isin"),
                "lei": company_data.get("lei"),
                "country": company_data.get("country"),
                "sector": company_data.get("sector")
            }
            client.post("/companies", json=create_data)
        
        return client
    
    def test_search_by_prefix_success(self, client_with_test_data):
        """Test searching companies by name prefix."""
        client = client_with_test_data
        
        response = client.get("/companies/search?prefix=A")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) >= 2  # Should find Apple and Amazon
        
        names = [item["name"] for item in data]
        assert any("Apple" in name for name in names)
        assert any("Amazon" in name for name in names)
    
    def test_search_by_prefix_with_limit(self, client_with_test_data):
        """Test searching with limit parameter."""
        client = client_with_test_data
        
        response = client.get("/companies/search?prefix=&limit=2")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) <= 2
    
    def test_search_missing_prefix(self, client_with_test_data):
        """Test search without prefix parameter."""
        client = client_with_test_data
        
        response = client.get("/companies/search")
        assert response.status_code == 422
    
    def test_search_empty_prefix(self, client_with_test_data):
        """Test search with empty prefix."""
        client = client_with_test_data
        
        response = client.get("/companies/search?prefix=")
        assert response.status_code == 422
    
    def test_search_no_results(self, client_with_test_data):
        """Test search with no matching results."""
        client = client_with_test_data
        
        response = client.get("/companies/search?prefix=XYZ")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 0
    
    def test_validate_existing_name(self, client_with_test_data):
        """Test validating an existing company name."""
        client = client_with_test_data
        
        response = client.get("/companies/validate?name=Apple Inc.")
        assert response.status_code == 200
        
        data = response.json()
        assert data["query"] == "Apple Inc."
        assert data["exists"] is True
        assert data["match"] is not None
        assert data["match"]["name"] == "Apple Inc."
    
    def test_validate_nonexistent_name(self, client_with_test_data):
        """Test validating a non-existent company name."""
        client = client_with_test_data
        
        response = client.get("/companies/validate?name=Nonexistent Company")
        assert response.status_code == 200
        
        data = response.json()
        assert data["query"] == "Nonexistent Company"
        assert data["exists"] is False
        assert data["match"] is None
    
    def test_validate_missing_name(self, client_with_test_data):
        """Test validation without name parameter."""
        client = client_with_test_data
        
        response = client.get("/companies/validate")
        assert response.status_code == 422
    
    def test_validate_empty_name(self, client_with_test_data):
        """Test validation with empty name."""
        client = client_with_test_data
        
        response = client.get("/companies/validate?name=")
        assert response.status_code == 422
    
    def test_lookup_by_ticker(self, client_with_test_data):
        """Test looking up company by ticker."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup?ticker=AAPL")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 1
        assert data[0]["ticker"] == "AAPL"
        assert data[0]["name"] == "Apple Inc."
    
    def test_lookup_by_lei(self, client_with_test_data):
        """Test looking up company by LEI."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup?lei=HWUPKR0MPOU8FGXBT394")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 1
        assert data[0]["lei"] == "HWUPKR0MPOU8FGXBT394"
        assert data[0]["name"] == "Apple Inc."
    
    def test_lookup_by_isin(self, client_with_test_data):
        """Test looking up company by ISIN."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup?isin=US0378331005")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 1
        assert data[0]["isin"] == "US0378331005"
        assert data[0]["name"] == "Apple Inc."
    
    def test_lookup_multiple_criteria(self, client_with_test_data):
        """Test looking up companies by multiple criteria."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup?ticker=AAPL&lei=XKZZ2JZF41MRHTR1V493")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 2  # Should find both Apple (ticker) and Microsoft (LEI)
    
    def test_lookup_no_criteria(self, client_with_test_data):
        """Test lookup without any criteria returns empty list."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 0
    
    def test_lookup_no_matches(self, client_with_test_data):
        """Test lookup with criteria that don't match."""
        client = client_with_test_data
        
        response = client.get("/companies/lookup?ticker=NONEXISTENT")
        assert response.status_code == 200
        
        data = response.json()
        assert len(data) == 0


class TestAPIValidation:
    """Test API validation and error handling."""
    
    def test_invalid_json_payload(self, mock_get_container):
        """Test handling invalid JSON payload."""
        client = TestClient(app)
        
        response = client.post("/companies", data="invalid json")
        assert response.status_code == 422
    
    def test_pydantic_validation_errors(self, mock_get_container):
        """Test Pydantic model validation errors."""
        client = TestClient(app)
        
        # Test with invalid field types
        invalid_data = {
            "name": "",  # Too short
            "ticker": 123,  # Wrong type
            "market_cap_usd": "not_a_number"  # Wrong type
        }
        
        response = client.post("/companies", json=invalid_data)
        assert response.status_code == 422
        
        error_detail = response.json()
        assert "detail" in error_detail
    
    def test_ticker_normalization(self, mock_get_container):
        """Test that ticker is normalized to uppercase."""
        client = TestClient(app)
        
        create_data = {
            "name": "Test Company",
            "ticker": "test"  # lowercase
        }
        
        response = client.post("/companies", json=create_data)
        assert response.status_code == 201
        
        data = response.json()
        assert data["ticker"] == "TEST"  # Should be uppercase


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_database_connection_error(self):
        """Test handling database connection errors."""
        client = TestClient(app)
        
        # Test with actual database configuration error
        # This should gracefully handle the missing credentials
        response = client.post("/companies", json={"name": "Test Company"})
        
        # The response depends on how the application handles the database error
        # It could be 500 (server error) or 503 (service unavailable)
        assert response.status_code in [500, 503, 422]
    
    def test_malformed_company_id_in_url(self, mock_get_container):
        """Test handling malformed company ID in URL path."""
        client = TestClient(app)
        
        # Test with special characters that might cause issues
        response = client.get("/companies/a/company%20with%20spaces")
        assert response.status_code == 404  # Not found is acceptable
    
    def test_extremely_long_search_prefix(self, mock_get_container):
        """Test handling extremely long search prefix."""
        client = TestClient(app)
        
        long_prefix = "a" * 1000
        response = client.get(f"/companies/search?prefix={long_prefix}")
        
        # Should handle gracefully without crashing
        assert response.status_code in [200, 422, 400]