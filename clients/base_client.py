"""
Base client providing common HTTP functionality for API testing.
Keeps individual client classes focused on endpoint-specific logic.
"""
import requests
from typing import Dict, Any, Optional


class BaseAPIClient:
    """Base class for API clients with common HTTP methods and error handling."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make GET request to endpoint."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, **kwargs)
        return response
    
    def post(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """Make POST request to endpoint."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=json_data, **kwargs)
        return response
    
    def put(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """Make PUT request to endpoint."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=json_data, **kwargs)
        return response
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make DELETE request to endpoint."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url, **kwargs)
        return response