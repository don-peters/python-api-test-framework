# Simplest possible API test - just make it work
import requests
#import jsonschema
import jsonschema
from helpers.request_helpers import make_get_request

BASE_URL = "https://jsonplaceholder.typicode.com"


# Refactoring to use helper function

def test_get_users():
    users = make_get_request("users")
    assert len(users) == 10

def test_get_single_user():
    user = make_get_request("users/1")
    assert user["id"] == 1
    assert "name" in user

def test_get_posts():
    posts = make_get_request("posts")
    assert len(posts) == 100

def test_get_comments():
    comments = make_get_request("comments")
    assert len(comments) == 500

def test_get_todos():
    todos = make_get_request("todos")
    assert len(todos) == 200

def test_get_single_user_not_found():
    make_get_request("users/999", expected_status=404)

def test_get_post_not_found():
    make_get_request("posts/999", expected_status=404)

def test_create_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }
    assert requests.post(f"{BASE_URL}/users", json=new_user).status_code == 201 
