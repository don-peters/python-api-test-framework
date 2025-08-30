
import requests
import jsonschema
import json
from pathlib import Path

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200
        return response.json()

    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        assert response.status_code == 200
        return response.json()
        self._validate_user_schema(response.json())
        

    def create_user(self, user_data):
        response = requests.post(f"{self.base_url}/users", json=user_data)
        assert response.status_code == 201
        return response.json()

    def update_user(self, user_id, user_data):
        response = requests.put(f"{self.base_url}/users/{user_id}", json=user_data)
        assert response.status_code == 200
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        assert response.status_code == 200
        if not response.content or response.content.strip() == b'':
            return {}
        return response.json()

    def _validate_user_schema(self, user_data):
        schema_path = Path(__file__).parent.parent / "schemas" / "user_schema.json"
        with open(schema_path, "r") as f:
            user_schema = json.load(f)
        try:
            jsonschema.validate(user_data, user_schema)
            return True
        except jsonschema.ValidationError as e:
            raise ValueError(f"User data validation failed: {e.message}")

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
