"""
JSONPlaceholder API client.
Provides simple, focused methods for each endpoint.
"""
import requests
from typing import Dict, Any, List
from .base_client import BaseAPIClient


class JSONPlaceholderClient(BaseAPIClient):
    """Client for JSONPlaceholder API endpoints."""
    
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")
    
    def get_users(self) -> requests.Response:
        """Get all users."""
        return self.get("users")
    
    def get_user(self, user_id: int) -> requests.Response:
        """Get user by ID."""
        return self.get(f"users/{user_id}")
    
    def create_user(self, user_data: Dict[str, Any]) -> requests.Response:
        """Create a new user."""
        return self.post("users", json_data=user_data)
    
    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> requests.Response:
        """Update existing user."""
        return self.put(f"users/{user_id}", json_data=user_data)
    
    def delete_user(self, user_id: int) -> requests.Response:
        """Delete user."""
        return self.delete(f"users/{user_id}")
    
    def get_posts(self) -> requests.Response:
        """Get all posts."""
        return self.get("posts")
    
    def get_post(self, post_id: int) -> requests.Response:
        """Get post by ID."""
        return self.get(f"posts/{post_id}")
    
    def get_user_posts(self, user_id: int) -> requests.Response:
        """Get posts by specific user."""
        return self.get("posts", params={"userId": user_id})