"""
Unit tests for the utils module.
"""
import pytest
from app.utils import normalize_name, derive_pk_from_name, non_empty


class TestNormalizeName:
    """Test the normalize_name function."""
    
    def test_normalize_basic_string(self):
        """Test normalizing a basic string."""
        result = normalize_name("Apple Inc.")
        assert result == "apple inc."
    
    def test_normalize_with_extra_spaces(self):
        """Test normalizing string with extra spaces."""
        result = normalize_name("  Apple   Inc.  ")
        assert result == "apple inc."
    
    def test_normalize_with_multiple_spaces(self):
        """Test normalizing string with multiple internal spaces."""
        result = normalize_name("Apple    Inc.     Corp")
        assert result == "apple inc. corp"
    
    def test_normalize_empty_string(self):
        """Test normalizing empty string."""
        result = normalize_name("")
        assert result == ""
    
    def test_normalize_whitespace_only(self):
        """Test normalizing whitespace-only string."""
        result = normalize_name("   ")
        assert result == ""
    
    def test_normalize_mixed_case(self):
        """Test normalizing mixed case string."""
        result = normalize_name("MicroSoft Corporation")
        assert result == "microsoft corporation"
    
    def test_normalize_special_characters(self):
        """Test normalizing string with special characters."""
        result = normalize_name("Johnson & Johnson")
        assert result == "johnson & johnson"
    
    def test_normalize_with_tabs_and_newlines(self):
        """Test normalizing string with tabs and newlines."""
        result = normalize_name("Apple\t\nInc.")
        assert result == "apple inc."


class TestDerivePkFromName:
    """Test the derive_pk_from_name function."""
    
    def test_derive_pk_normal_name(self):
        """Test deriving partition key from normal name."""
        result = derive_pk_from_name("Apple Inc.")
        assert result == "a"
    
    def test_derive_pk_with_leading_space(self):
        """Test deriving partition key from name with leading space."""
        result = derive_pk_from_name("  Microsoft Corp")
        assert result == "m"
    
    def test_derive_pk_empty_string(self):
        """Test deriving partition key from empty string."""
        result = derive_pk_from_name("")
        assert result == "_"
    
    def test_derive_pk_whitespace_only(self):
        """Test deriving partition key from whitespace-only string."""
        result = derive_pk_from_name("   ")
        assert result == "_"
    
    def test_derive_pk_uppercase_name(self):
        """Test deriving partition key from uppercase name."""
        result = derive_pk_from_name("AMAZON.COM INC")
        assert result == "a"
    
    def test_derive_pk_numeric_start(self):
        """Test deriving partition key from name starting with number."""
        result = derive_pk_from_name("3M Company")
        assert result == "3"
    
    def test_derive_pk_special_character_start(self):
        """Test deriving partition key from name starting with special character."""
        result = derive_pk_from_name("@Home Corporation")
        assert result == "@"


class TestNonEmpty:
    """Test the non_empty function."""
    
    def test_non_empty_valid_string(self):
        """Test non_empty with valid string."""
        assert non_empty("Apple") is True
        assert non_empty("A") is True
        assert non_empty("123") is True
    
    def test_non_empty_empty_string(self):
        """Test non_empty with empty string."""
        assert non_empty("") is False
    
    def test_non_empty_whitespace_only(self):
        """Test non_empty with whitespace-only string."""
        assert non_empty("   ") is False
        assert non_empty("\t\n") is False
    
    def test_non_empty_none_value(self):
        """Test non_empty with None value."""
        assert non_empty(None) is False
    
    def test_non_empty_non_string_types(self):
        """Test non_empty with non-string types."""
        assert non_empty(123) is False
        assert non_empty([]) is False
        assert non_empty({}) is False
        assert non_empty(True) is False
    
    def test_non_empty_string_with_content_and_spaces(self):
        """Test non_empty with string that has content and spaces."""
        assert non_empty("  Apple  ") is True
        assert non_empty("\tMicrosoft\n") is True


class TestUtilsIntegration:
    """Integration tests for utils functions working together."""
    
    def test_normalize_and_derive_pk_workflow(self):
        """Test the typical workflow of normalizing and deriving partition key."""
        company_name = "  APPLE Inc.  "
        normalized = normalize_name(company_name)
        pk = derive_pk_from_name(company_name)
        
        assert normalized == "apple inc."
        assert pk == "a"
    
    def test_edge_case_empty_name_workflow(self):
        """Test workflow with empty company name."""
        company_name = ""
        normalized = normalize_name(company_name)
        pk = derive_pk_from_name(company_name)
        
        assert normalized == ""
        assert pk == "_"
    
    def test_validation_workflow(self):
        """Test validation workflow using non_empty."""
        valid_names = ["Apple Inc.", "Microsoft"]
        invalid_names = ["", "   ", None]
        
        for name in valid_names:
            assert non_empty(name) is True
            if non_empty(name):
                normalized = normalize_name(name)
                pk = derive_pk_from_name(name)
                assert len(normalized) > 0
                assert pk != "_"
        
        for name in invalid_names:
            assert non_empty(name) is False