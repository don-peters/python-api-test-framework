# # Real validation, authentication, persistence
# import requests
# import jsonschema
# from helpers.request_helpers import make_get_request, make_post_request

# GOREST_TOKEN = "3b783a032897ec01f41f1d38309b51dd220b2d1f17c962d37462780c87dd9cb9"
# GOREST_BASE = "https://gorest.co.in/public/v2"

# def test_create_user_with_invalid_request():
#     headers = {"Authorization": f"Bearer {GOREST_TOKEN}"}
    
#     # This will actually validate required fields!
#     invalid_user = {}
#     response = requests.post(f"{GOREST_BASE}/users", json=invalid_user, headers=headers)
#     assert response.status_code == 422  # Real validation error!
    
# def test_create_new_user():
#     headers = {"Authorization": f"Bearer {GOREST_TOKEN}"}
#          # Valid user creation
#     valid_user = {"name": "John", "email": "john@example.com", "gender": "male", "status": "active"}
#     response = requests.post(f"{GOREST_BASE}/users", json=valid_user, headers=headers)
#     assert response.status_code == 201

