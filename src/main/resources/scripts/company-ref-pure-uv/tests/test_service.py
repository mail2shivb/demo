"""
Unit tests for the CompanyService class.
"""
import pytest
from unittest.mock import Mock, MagicMock
from app.services.company_service import CompanyService
from app.repository.company_repository import CompanyRepository


class TestCompanyService:
    """Test the CompanyService class."""
    
    @pytest.fixture
    def mock_repository(self):
        """Create a mock repository."""
        return Mock(spec=CompanyRepository)
    
    @pytest.fixture
    def service(self, mock_repository):
        """Create service instance with mocked repository."""
        return CompanyService(repo=mock_repository)
    
    def test_service_initialization_with_repo(self, mock_repository):
        """Test service initialization with provided repository."""
        service = CompanyService(repo=mock_repository)
        assert service.repo == mock_repository
    
    def test_service_initialization_without_repo(self):
        """Test service initialization creates default repository."""
        service = CompanyService()
        assert isinstance(service.repo, CompanyRepository)
    
    def test_create_company(self, service, mock_repository, sample_company_data):
        """Test creating a company through service."""
        expected_result = {**sample_company_data, "id": "123", "pk": "a"}
        mock_repository.create.return_value = expected_result
        
        result = service.create_company(sample_company_data)
        
        mock_repository.create.assert_called_once_with(sample_company_data)
        assert result == expected_result
    
    def test_get_company(self, service, mock_repository):
        """Test getting a company through service."""
        expected_result = {"id": "123", "pk": "a", "name": "Apple Inc."}
        mock_repository.get.return_value = expected_result
        
        result = service.get_company("123", "a")
        
        mock_repository.get.assert_called_once_with("123", "a")
        assert result == expected_result
    
    def test_get_company_not_found(self, service, mock_repository):
        """Test getting non-existent company returns None."""
        mock_repository.get.return_value = None
        
        result = service.get_company("nonexistent", "n")
        
        mock_repository.get.assert_called_once_with("nonexistent", "n")
        assert result is None
    
    def test_update_company(self, service, mock_repository):
        """Test updating a company through service."""
        update_data = {"sector": "Technology"}
        expected_result = {"id": "123", "pk": "a", "name": "Apple Inc.", "sector": "Technology"}
        mock_repository.update.return_value = expected_result
        
        result = service.update_company("123", "a", update_data)
        
        mock_repository.update.assert_called_once_with("123", "a", update_data)
        assert result == expected_result
    
    def test_update_company_not_found(self, service, mock_repository):
        """Test updating non-existent company returns None."""
        mock_repository.update.return_value = None
        
        result = service.update_company("nonexistent", "n", {"sector": "Tech"})
        
        mock_repository.update.assert_called_once_with("nonexistent", "n", {"sector": "Tech"})
        assert result is None
    
    def test_delete_company_success(self, service, mock_repository):
        """Test successfully deleting a company."""
        mock_repository.delete.return_value = True
        
        result = service.delete_company("123", "a")
        
        mock_repository.delete.assert_called_once_with("123", "a")
        assert result is True
    
    def test_delete_company_not_found(self, service, mock_repository):
        """Test deleting non-existent company returns False."""
        mock_repository.delete.return_value = False
        
        result = service.delete_company("nonexistent", "n")
        
        mock_repository.delete.assert_called_once_with("nonexistent", "n")
        assert result is False
    
    def test_search_by_name_prefix(self, service, mock_repository):
        """Test searching companies by name prefix."""
        expected_results = [
            {"id": "1", "name": "Apple Inc."},
            {"id": "2", "name": "Amazon.com Inc."}
        ]
        mock_repository.search_by_name_prefix.return_value = expected_results
        
        result = service.search_by_name_prefix("A")
        
        mock_repository.search_by_name_prefix.assert_called_once_with("A", 20)
        assert result == expected_results
    
    def test_search_by_name_prefix_with_limit(self, service, mock_repository):
        """Test searching companies by name prefix with custom limit."""
        expected_results = [{"id": "1", "name": "Apple Inc."}]
        mock_repository.search_by_name_prefix.return_value = expected_results
        
        result = service.search_by_name_prefix("A", limit=5)
        
        mock_repository.search_by_name_prefix.assert_called_once_with("A", 5)
        assert result == expected_results
    
    def test_search_by_name_prefix_no_results(self, service, mock_repository):
        """Test searching with no results."""
        mock_repository.search_by_name_prefix.return_value = []
        
        result = service.search_by_name_prefix("XYZ")
        
        mock_repository.search_by_name_prefix.assert_called_once_with("XYZ", 20)
        assert result == []
    
    def test_validate_name_exists_found(self, service, mock_repository):
        """Test validating name that exists."""
        company_data = {"id": "123", "name": "Apple Inc."}
        mock_repository.find_by_name_exact.return_value = company_data
        
        result = service.validate_name_exists("Apple Inc.")
        
        mock_repository.find_by_name_exact.assert_called_once_with("Apple Inc.")
        assert result["query"] == "Apple Inc."
        assert result["exists"] is True
        assert result["match"]["id"] == "123"
        assert result["match"]["name"] == "Apple Inc."
    
    def test_validate_name_exists_not_found(self, service, mock_repository):
        """Test validating name that doesn't exist."""
        mock_repository.find_by_name_exact.return_value = None
        
        result = service.validate_name_exists("Nonexistent Company")
        
        mock_repository.find_by_name_exact.assert_called_once_with("Nonexistent Company")
        assert result["query"] == "Nonexistent Company"
        assert result["exists"] is False
        assert result["match"] is None
    
    def test_find_by_keys_ticker(self, service, mock_repository):
        """Test finding companies by ticker."""
        expected_results = [{"id": "123", "ticker": "AAPL", "name": "Apple Inc."}]
        mock_repository.find_by_keys.return_value = expected_results
        
        result = service.find_by_keys(ticker="AAPL")
        
        mock_repository.find_by_keys.assert_called_once_with(ticker="AAPL")
        assert result == expected_results
    
    def test_find_by_keys_multiple_criteria(self, service, mock_repository):
        """Test finding companies by multiple criteria."""
        expected_results = [
            {"id": "123", "ticker": "AAPL", "name": "Apple Inc."},
            {"id": "456", "lei": "XKZZ2JZF41MRHTR1V493", "name": "Microsoft Corporation"}
        ]
        mock_repository.find_by_keys.return_value = expected_results
        
        result = service.find_by_keys(ticker="AAPL", lei="XKZZ2JZF41MRHTR1V493")
        
        mock_repository.find_by_keys.assert_called_once_with(ticker="AAPL", lei="XKZZ2JZF41MRHTR1V493")
        assert result == expected_results
    
    def test_find_by_keys_no_results(self, service, mock_repository):
        """Test finding companies with no matches."""
        mock_repository.find_by_keys.return_value = []
        
        result = service.find_by_keys(ticker="NONEXISTENT")
        
        mock_repository.find_by_keys.assert_called_once_with(ticker="NONEXISTENT")
        assert result == []


class TestCompanyServiceIntegration:
    """Integration tests for CompanyService with real repository."""
    
    @pytest.fixture
    def service_with_mock_container(self, mock_container):
        """Create service with repository using mock container."""
        from app.repository.company_repository import CompanyRepository
        repo = CompanyRepository()
        repo._container = mock_container
        return CompanyService(repo=repo)
    
    def test_full_company_lifecycle(self, service_with_mock_container, sample_company_data):
        """Test complete CRUD lifecycle through service."""
        service = service_with_mock_container
        
        # Create
        created = service.create_company(sample_company_data)
        assert created["name"] == sample_company_data["name"]
        assert "id" in created
        assert "pk" in created
        
        # Read
        retrieved = service.get_company(created["id"], created["pk"])
        assert retrieved is not None
        assert retrieved["name"] == sample_company_data["name"]
        
        # Update
        update_data = {"sector": "Consumer Electronics"}
        updated = service.update_company(created["id"], created["pk"], update_data)
        assert updated is not None
        assert updated["sector"] == "Consumer Electronics"
        
        # Delete
        deleted = service.delete_company(created["id"], created["pk"])
        assert deleted is True
        
        # Verify deletion
        not_found = service.get_company(created["id"], created["pk"])
        assert not_found is None
    
    def test_search_and_validation_workflow(self, service_with_mock_container, sample_companies_list):
        """Test search and validation workflow."""
        service = service_with_mock_container
        
        # Create multiple companies
        for company_data in sample_companies_list:
            service.create_company(company_data)
        
        # Search by prefix
        search_results = service.search_by_name_prefix("A")
        assert len(search_results) >= 2  # Apple and Amazon
        
        # Validate existing name
        validation_result = service.validate_name_exists("Apple Inc.")
        assert validation_result["exists"] is True
        assert validation_result["match"] is not None
        
        # Validate non-existing name
        validation_result = service.validate_name_exists("Nonexistent Company")
        assert validation_result["exists"] is False
        assert validation_result["match"] is None
    
    def test_key_lookup_workflow(self, service_with_mock_container, sample_companies_list):
        """Test key-based lookup workflow."""
        service = service_with_mock_container
        
        # Create companies
        for company_data in sample_companies_list:
            service.create_company(company_data)
        
        # Find by ticker
        ticker_results = service.find_by_keys(ticker="AAPL")
        assert len(ticker_results) == 1
        assert ticker_results[0]["name"] == "Apple Inc."
        
        # Find by LEI
        lei_results = service.find_by_keys(lei="HWUPKR0MPOU8FGXBT394")
        assert len(lei_results) == 1
        assert lei_results[0]["name"] == "Apple Inc."
        
        # Find by multiple criteria (OR logic)
        multi_results = service.find_by_keys(ticker="AAPL", lei="XKZZ2JZF41MRHTR1V493")
        assert len(multi_results) == 2  # Apple (ticker) and Microsoft (LEI)