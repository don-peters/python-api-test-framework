"""
Schema validation tests demonstrating validation patterns.
These tests focus specifically on data structure validation.
"""
import pytest
import allure
from test_data.users import UserTestData
from utils.assertions import assert_json_schema


@allure.feature("Schema Validation")
class TestSchemaValidation:
    """Test suite for JSON schema validation patterns."""
    
    @allure.story("User Schema")
    @allure.title("Valid user data passes schema validation")
    def test_valid_user_passes_schema(self):
        """Test that properly structured user data passes validation."""
        # Arrange
        user_data = UserTestData.valid_user()
        # Add required fields that API would include
        user_data.update({
            "id": 1,
            "address": {
                "street": "123 Main St",
                "city": "Anytown", 
                "zipcode": "12345"
            },
            "company": {
                "name": "Test Company"
            }
        })
        
        # Act & Assert
        assert_json_schema(user_data, "user")
    
    @allure.story("User Schema")  
    @allure.title("Minimal user data passes schema validation")
    def test_minimal_user_passes_schema(self):
        """Test that user with only required fields passes validation."""
        # Arrange
        minimal_user = {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
        
        # Act & Assert
        assert_json_schema(minimal_user, "user")
    
    @allure.story("User Schema")
    @allure.title("User with missing required fields fails validation")
    def test_missing_required_fields_fails_validation(self):
        """Test that user missing required fields fails validation."""
        # Arrange
        incomplete_user = {
            "id": 1,
            "name": "Test User"
            # Missing username and email
        }
        
        # Act & Assert
        with pytest.raises(AssertionError, match="does not match user schema"):
            assert_json_schema(incomplete_user, "user")
    
    @allure.story("User Schema")
    @allure.title("User with wrong data types fails validation")
    def test_wrong_data_types_fail_validation(self):
        """Test that wrong data types fail validation."""
        # Arrange - test different type violations
        test_cases = [
            {
                "name": "Non-integer ID",
                "data": {
                    "id": "not_an_integer",  # Should be integer
                    "name": "Test User",
                    "username": "testuser", 
                    "email": "test@example.com"
                }
            },
            {
                "name": "Non-string email", 
                "data": {
                    "id": 1,
                    "name": "Test User",
                    "username": "testuser",
                    "email": 123  # Should be string
                }
            }
        ]
        
        for test_case in test_cases:
            with pytest.raises(AssertionError, match="does not match user schema"):
                assert_json_schema(test_case["data"], "user")
    
    @allure.story("Users List Schema")
    @allure.title("Valid users list passes schema validation")
    def test_users_list_passes_schema(self):
        """Test that list of users passes list schema validation."""
        # Arrange
        users_list = [
            {
                "id": 1,
                "name": "User One",
                "username": "user1",
                "email": "user1@example.com"
            },
            {
                "id": 2, 
                "name": "User Two",
                "username": "user2",
                "email": "user2@example.com"
            }
        ]
        
        # Act & Assert
        assert_json_schema(users_list, "users_list")