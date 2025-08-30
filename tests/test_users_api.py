"""
User API endpoint tests demonstrating clean test patterns.
Each test follows arrange/act/assert pattern for maximum readability.
"""
import pytest
import allure
from clients.jsonplaceholder_client import JSONPlaceholderClient
from test_data.users import UserTestData
from utils.assertions import (
    assert_status_code,
    assert_json_schema,
    assert_contains_keys,
    assert_not_empty,
    assert_response_time
)


@allure.feature("Users API")
class TestUsersAPI:
    """Test suite for user-related API endpoints."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test client."""
        self.client = JSONPlaceholderClient()
    
    @allure.story("Get Users")
    @allure.title("Get all users returns valid list")
    def test_get_all_users_success(self):
        """Test retrieving all users returns valid response."""
        # Arrange - no setup needed
        
        # Act
        response = self.client.get_users()
        
        # Assert
        assert_status_code(response, 200)
        assert_response_time(response, 2.0)
        
        users_list = response.json()
        assert_not_empty(users_list)
        assert_json_schema(users_list, "users_list")
    
    @allure.story("Get User")
    @allure.title("Get single user by ID returns valid user")
    def test_get_single_user_success(self):
        """Test retrieving single user by ID."""
        # Arrange
        user_id = 1
        
        # Act
        response = self.client.get_user(user_id)
        
        # Assert
        assert_status_code(response, 200)
        assert_response_time(response, 2.0)
        
        user_data = response.json()
        assert_contains_keys(user_data, ["id", "name", "username", "email"])
        assert_json_schema(user_data, "user")
        assert user_data["id"] == user_id
    
    @allure.story("Get User")
    @allure.title("Get nonexistent user returns 404")
    def test_get_nonexistent_user_returns_404(self):
        """Test requesting nonexistent user returns appropriate error."""
        # Arrange
        nonexistent_id = 999999
        
        # Act
        response = self.client.get_user(nonexistent_id)
        
        # Assert
        assert_status_code(response, 404)
    
    @allure.story("Create User")
    @allure.title("Create user with valid data succeeds")
    def test_create_user_success(self):
        """Test creating user with valid data."""
        # Arrange
        user_data = UserTestData.valid_user()
        
        # Act
        response = self.client.create_user(user_data)
        
        # Assert
        assert_status_code(response, 201)
        
        created_user = response.json()
        assert_contains_keys(created_user, ["id", "name", "username", "email"])
        assert_json_schema(created_user, "user")
        
        # Verify submitted data is preserved
        assert created_user["name"] == user_data["name"]
        assert created_user["email"] == user_data["email"]
    
    @allure.story("Update User")
    @allure.title("Update existing user succeeds")
    def test_update_user_success(self):
        """Test updating existing user."""
        # Arrange
        user_id = 1
        update_data = UserTestData.update_data()
        
        # Act
        response = self.client.update_user(user_id, update_data)
        
        # Assert
        assert_status_code(response, 200)
        
        updated_user = response.json()
        assert_json_schema(updated_user, "user_partial")
        assert updated_user["id"] == user_id
        assert updated_user["name"] == update_data["name"]
    
    @allure.story("Delete User")
    @allure.title("Delete user succeeds")
    def test_delete_user_success(self):
        """Test deleting user."""
        # Arrange
        user_id = 1
        
        # Act
        response = self.client.delete_user(user_id)
        
        # Assert
        assert_status_code(response, 200)