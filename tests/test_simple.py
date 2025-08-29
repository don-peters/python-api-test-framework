
import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_users(api_client):
    users = api_client.get_users()
    assert len(users) == 10

@pytest.mark.regression
def test_get_single_user(api_client):
    user = api_client.get_user("1")
    assert user["id"] == 1
    assert "name" in user

def test_create_user(api_client):
    new_user = {"name": "Alice", "username": "alice123", "email": "alice123@testmail.com"}
    created_user = api_client.create_user(new_user)
    assert created_user["name"] == new_user["name"]


def test_server_error_handling(httpbin_client):
    response = httpbin_client.get_status_code(500)
    assert response.status_code == 500

def test_client_error_handling(httpbin_client):
    response = httpbin_client.get_status_code(404)
    assert response.status_code == 404
    

