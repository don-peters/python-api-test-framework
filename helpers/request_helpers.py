import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def make_get_request(endpoint, expected_status=200):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    assert response.status_code == expected_status
    assert "application/json" in response.headers["Content-Type"]
    return response.json()
