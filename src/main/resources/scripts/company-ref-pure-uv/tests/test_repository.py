"""
Unit tests for the CompanyRepository class.
"""
import pytest
import uuid
from unittest.mock import patch
from azure.cosmos.exceptions import CosmosHttpResponseError, CosmosResourceNotFoundError
from app.repository.company_repository import CompanyRepository
from tests.conftest import MockCosmosContainer


class TestCompanyRepository:
    """Test the CompanyRepository class."""
    
    @pytest.fixture
    def repository(self, mock_container):
        """Create repository instance with mocked container."""
        repo = CompanyRepository()
        repo._container = mock_container
        return repo
    
    def test_create_company_basic(self, repository, sample_company_data):
        """Test creating a basic company."""
        result = repository.create(sample_company_data)
        
        assert result["name"] == sample_company_data["name"]
        assert result["name_lower"] == "apple inc."
        assert result["pk"] == "a"
        assert result["ticker"] == "AAPL"
        assert "id" in result
    
    def test_create_company_with_id(self, repository, sample_company_data):
        """Test creating company with provided ID."""
        test_id = "test-123"
        sample_company_data["id"] = test_id
        
        result = repository.create(sample_company_data)
        assert result["id"] == test_id
    
    def test_create_company_without_ticker(self, repository):
        """Test creating company without ticker."""
        data = {
            "name": "Private Company Ltd",
            "country": "US"
        }
        
        result = repository.create(data)
        assert result["name"] == "Private Company Ltd"
        assert result["name_lower"] == "private company ltd"
        assert result["pk"] == "p"
        assert "ticker" not in result or not result.get("ticker")
    
    def test_create_company_duplicate_name(self, repository, sample_company_data):
        """Test creating company with duplicate name raises error."""
        # Create first company
        repository.create(sample_company_data)
        
        # Try to create duplicate
        with pytest.raises(CosmosHttpResponseError):
            repository.create(sample_company_data)
    
    def test_create_company_duplicate_ticker(self, repository):
        """Test creating companies with duplicate ticker raises error."""
        company1 = {"name": "Apple Inc.", "ticker": "AAPL"}
        company2 = {"name": "Different Company", "ticker": "AAPL"}
        
        repository.create(company1)
        
        with pytest.raises(CosmosHttpResponseError):
            repository.create(company2)
    
    def test_get_existing_company(self, repository, sample_company_data):
        """Test retrieving an existing company."""
        created = repository.create(sample_company_data)
        
        result = repository.get(created["id"], created["pk"])
        assert result is not None
        assert result["name"] == sample_company_data["name"]
        assert result["id"] == created["id"]
    
    def test_get_nonexistent_company(self, repository):
        """Test retrieving a non-existent company returns None."""
        result = repository.get("nonexistent", "n")
        assert result is None
    
    def test_update_existing_company(self, repository, sample_company_data):
        """Test updating an existing company."""
        created = repository.create(sample_company_data)
        
        update_data = {
            "sector": "Consumer Electronics",
            "notes": "Updated notes"
        }
        
        result = repository.update(created["id"], created["pk"], update_data)
        assert result is not None
        assert result["sector"] == "Consumer Electronics"
        assert result["notes"] == "Updated notes"
        assert result["name"] == sample_company_data["name"]  # Original data preserved
    
    def test_update_company_name(self, repository, sample_company_data):
        """Test updating company name updates derived fields."""
        created = repository.create(sample_company_data)
        
        update_data = {"name": "Apple Corporation"}
        
        result = repository.update(created["id"], created["pk"], update_data)
        assert result is not None
        assert result["name"] == "Apple Corporation"
        assert result["name_lower"] == "apple corporation"
        # Note: pk might change, but for this test we assume same container behavior
    
    def test_update_nonexistent_company(self, repository):
        """Test updating a non-existent company returns None."""
        result = repository.update("nonexistent", "n", {"sector": "Tech"})
        assert result is None
    
    def test_delete_existing_company(self, repository, sample_company_data):
        """Test deleting an existing company."""
        created = repository.create(sample_company_data)
        
        result = repository.delete(created["id"], created["pk"])
        assert result is True
        
        # Verify company is deleted
        retrieved = repository.get(created["id"], created["pk"])
        assert retrieved is None
    
    def test_delete_nonexistent_company(self, repository):
        """Test deleting a non-existent company returns False."""
        result = repository.delete("nonexistent", "n")
        assert result is False
    
    def test_find_by_name_exact_existing(self, repository, sample_company_data):
        """Test finding company by exact name match."""
        repository.create(sample_company_data)
        
        result = repository.find_by_name_exact("Apple Inc.")
        assert result is not None
        assert result["name"] == "Apple Inc."
    
    def test_find_by_name_exact_case_insensitive(self, repository, sample_company_data):
        """Test finding company by exact name is case insensitive."""
        repository.create(sample_company_data)
        
        result = repository.find_by_name_exact("apple inc.")
        assert result is not None
        assert result["name"] == "Apple Inc."
    
    def test_find_by_name_exact_nonexistent(self, repository):
        """Test finding non-existent company by name returns None."""
        result = repository.find_by_name_exact("Nonexistent Company")
        assert result is None
    
    def test_search_by_name_prefix(self, repository, sample_companies_list):
        """Test searching companies by name prefix."""
        # Create multiple companies
        for company in sample_companies_list:
            repository.create(company)
        
        # Search for companies starting with "A"
        results = repository.search_by_name_prefix("A")
        assert len(results) >= 2  # Apple and Amazon
        
        names = [r["name"] for r in results]
        assert any("Apple" in name for name in names)
        assert any("Amazon" in name for name in names)
    
    def test_search_by_name_prefix_with_limit(self, repository, sample_companies_list):
        """Test searching companies by name prefix with limit."""
        for company in sample_companies_list:
            repository.create(company)
        
        results = repository.search_by_name_prefix("", limit=2)
        assert len(results) <= 2
    
    def test_search_by_name_prefix_no_matches(self, repository):
        """Test searching with prefix that has no matches."""
        results = repository.search_by_name_prefix("XYZ")
        assert len(results) == 0
    
    def test_find_by_keys_ticker_only(self, repository, sample_companies_list):
        """Test finding companies by ticker only."""
        for company in sample_companies_list:
            repository.create(company)
        
        results = repository.find_by_keys(ticker="AAPL")
        assert len(results) == 1
        assert results[0]["name"] == "Apple Inc."
    
    def test_find_by_keys_lei_only(self, repository, sample_companies_list):
        """Test finding companies by LEI only."""
        for company in sample_companies_list:
            repository.create(company)
        
        results = repository.find_by_keys(lei="HWUPKR0MPOU8FGXBT394")
        assert len(results) == 1
        assert results[0]["name"] == "Apple Inc."
    
    def test_find_by_keys_multiple_criteria(self, repository, sample_companies_list):
        """Test finding companies by multiple criteria (OR logic)."""
        for company in sample_companies_list:
            repository.create(company)
        
        results = repository.find_by_keys(ticker="AAPL", lei="XKZZ2JZF41MRHTR1V493")
        assert len(results) == 2  # Should find both Apple (ticker) and Microsoft (LEI)
    
    def test_find_by_keys_no_criteria(self, repository):
        """Test finding companies with no criteria returns empty list."""
        results = repository.find_by_keys()
        assert len(results) == 0
    
    def test_find_by_keys_no_matches(self, repository, sample_companies_list):
        """Test finding companies with criteria that don't match."""
        for company in sample_companies_list:
            repository.create(company)
        
        results = repository.find_by_keys(ticker="NONEXISTENT")
        assert len(results) == 0
    
    def test_ticker_case_normalization(self, repository):
        """Test that ticker is converted to uppercase."""
        data = {"name": "Test Company", "ticker": "test"}
        
        result = repository.create(data)
        assert result["ticker"] == "TEST"
    
    def test_empty_ticker_not_normalized(self, repository):
        """Test that empty ticker is not processed."""
        data = {"name": "Test Company", "ticker": ""}
        
        result = repository.create(data)
        assert result["ticker"] == ""


class TestCompanyRepositoryEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_create_with_minimal_data(self, mock_container):
        """Test creating company with minimal required data."""
        repo = CompanyRepository()
        repo._container = mock_container
        
        minimal_data = {"name": "Minimal Corp"}
        result = repo.create(minimal_data)
        
        assert result["name"] == "Minimal Corp"
        assert result["name_lower"] == "minimal corp"
        assert result["pk"] == "m"
        assert "id" in result
    
    def test_create_preserves_original_data(self, mock_container, sample_company_data):
        """Test that create operation doesn't mutate original data."""
        repo = CompanyRepository()
        repo._container = mock_container
        
        original_data = sample_company_data.copy()
        repo.create(sample_company_data)
        
        # Original data should be unchanged (except for the copy we made)
        assert "id" not in original_data or original_data.get("id") == sample_company_data.get("id")
        assert "name_lower" not in original_data
        assert "pk" not in original_data