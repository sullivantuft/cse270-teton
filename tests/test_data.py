import requests

# ============================================================
# Test 1: JSON response for /data/all
# ============================================================
def test_data_endpoint(requests_mock):
    requests_mock.get(
        "http://127.0.0.1:8000/data/all",
        json={"businesses": [{"name": "Teton Elementary"}]},
        status_code=200,
    )

    response = requests.get("http://127.0.0.1:8000/data/all")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "businesses" in data
    assert isinstance(data["businesses"], list)
    assert data["businesses"][0]["name"] == "Teton Elementary"


# ============================================================
# Test 2: Empty TEXT response for URL with parameters
# ============================================================
def test_data_endpoint_with_params(requests_mock):
    requests_mock.get(
        "http://127.0.0.1:8000/data/all",
        text="",   # empty response body
        status_code=200
    )

    response = requests.get(
        "http://127.0.0.1:8000/data/all",
        params={"username": "admin", "password": "qwerty"}
    )

    assert response.status_code == 200

    # Try JSON first, fall back to text
    try:
        content = response.json()
    except ValueError:
        content = response.text

    assert content == ""
