import requests

BASE_URL = "http://127.0.0.1:8000/users"

# ============================================================
# Unauthorized login test
# ============================================================
def test_get_users_unauthorized(requests_mock):
    requests_mock.get(
        BASE_URL,
        text="",     # empty body
        status_code=401
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "admin"
    })

    assert response.status_code == 401
    assert response.text == ""


# ============================================================
# Successful login test
# ============================================================
def test_get_users_authorized(requests_mock):
    requests_mock.get(
        BASE_URL,
        text="",    # empty body
        status_code=200
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "qwerty"
    })

    assert response.status_code == 200
    assert response.text == ""
