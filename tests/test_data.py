import pytest
import requests
import responses


# ============================================================
# Test 1: JSON response for /data/all
# ============================================================
@responses.activate
def test_data_endpoint():
    # Mocked JSON response
    responses.add(
        responses.GET,
        "http://127.0.0.1:8000/data/all",
        json={"businesses": [{"name": "Teton Elementary"}]},
        status=200
    )

    response = requests.get("http://127.0.0.1:8000/data/all")

    # Status code check
    assert response.status_code == 200

    # JSON structure checks
    data = response.json()
    assert isinstance(data, dict)
    assert "businesses" in data

    businesses = data["businesses"]
    assert isinstance(businesses, list)
    assert len(businesses) > 0

    first = businesses[0]
    assert isinstance(first, dict)
    assert first["name"] == "Teton Elementary"


# ============================================================
# Test 2: Empty TEXT response for URL with parameters
# ============================================================
@responses.activate
def test_data_endpoint_with_params():
    # URL with expected query parameters
    responses.add(
        responses.GET,
        "http://127.0.0.1:8000/data/all?username=admin&password=qwerty",
        body="",   # empty text response
        status=200,
        content_type="text/plain"
    )

    response = requests.get(
        "http://127.0.0.1:8000/data/all",
        params={"username": "admin", "password": "qwerty"}
    )

    assert response.status_code == 200

    # Accept text OR empty JSON safely
    try:
        content = response.json()
    except ValueError:
        content = response.text

    # For this test, it must be completely empty
    assert content == ""
