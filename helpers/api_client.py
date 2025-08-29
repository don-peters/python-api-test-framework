import requests
import jsonschema
import json
import os

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
    
    def get_users(self):
        # Move your GET logic here - let Copilot suggest the implementation 
        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200
        return response.json()

    
    def get_user(self, user_id):
        # Let Copilot suggest this method
        response = requests.get(f"{self.base_url}/users/{user_id}")
        assert response.status_code == 200
        return response.json()
        
    def create_user(self, user_data):
        # Let Copilot suggest this method
        response = requests.post(f"{self.base_url}/users", json=user_data)
        assert response.status_code == 201
        return response.json()
        
    def update_user(self, user_id, user_data):
        # Let Copilot suggest this method
        response = requests.put(f"{self.base_url}/users/{user_id}", json=user_data)
        assert response.status_code == 200
        return response.json()
        
    def delete_user(self, user_id):
        # Let Copilot suggest this method
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        assert response.status_code == 200
        return response
    
class HTTPBinClient:
    def __init__(self):
        self.base_url = "https://httpbin.org"
    
    def get_status_code(self, code):
        response = requests.get(f"{self.base_url}/status/{code}")
        assert response.status_code == code
        return response
    
    def get_post_echo(self, data):
        response = requests.post(f"{self.base_url}/post", json=data)
        return response.json()
