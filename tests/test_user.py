import requests

def test_get_users_unauthorized():
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(url, params=params)

    # Expect 401 Unauthorized
    assert response.status_code == 401

    # Expect an empty body
    assert response.text.strip() == ""
