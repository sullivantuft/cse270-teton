import requests

BASE_URL = "http://127.0.0.1:8000/users"


def test_get_users_unauthorized(requests_mock):
    # Mock the base URL — DO NOT include ?username=... etc
    requests_mock.get(
        BASE_URL,
        text="",
        status_code=401,
        complete_qs=False  # allow any query string to match
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "admin"
    })

    assert response.status_code == 401
    assert response.text == ""


def test_get_users_authorized(requests_mock):
    requests_mock.get(
        BASE_URL,
        text="",
        status_code=200,
        complete_qs=False  # allow any query string to match
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "qwerty"
    })

    assert response.status_code == 200
    assert response.text == ""
