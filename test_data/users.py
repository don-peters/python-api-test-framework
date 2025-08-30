"""
Test data factories for user-related tests.
Keeps test data organized and makes tests more readable.
"""
from typing import Dict, Any


class UserTestData:
    """Factory for creating user test data."""
    
    @staticmethod
    def valid_user() -> Dict[str, Any]:
        """Standard valid user data for testing."""
        return {
            "name": "John Doe",
            "username": "johndoe",
            "email": "john.doe@example.com",
            "phone": "555-0123",
            "website": "johndoe.com"
        }
    
    @staticmethod
    def minimal_user() -> Dict[str, Any]:
        """User with only required fields."""
        return {
            "name": "Jane Smith",
            "username": "janesmith", 
            "email": "jane.smith@example.com"
        }
    
    @staticmethod
    def invalid_email_user() -> Dict[str, Any]:
        """User with invalid email format."""
        return {
            "name": "Bad Email User",
            "username": "bademail",
            "email": "not-an-email"
        }
    
    @staticmethod
    def missing_required_fields() -> Dict[str, Any]:
        """User missing required fields."""
        return {
            "phone": "555-0123"
            # Missing name, username, email
        }
    
    @staticmethod
    def update_data() -> Dict[str, Any]:
        """Partial data for user updates."""
        return {
            "name": "Updated Name",
            "email": "updated@example.com"
        }