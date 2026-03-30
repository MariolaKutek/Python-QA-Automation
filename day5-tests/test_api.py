import pytest
import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


def test_response_time():
    start = time.time()
    response = requests.get(f"{BASE_URL}/users")
    end = time.time()

    response_time = end - start
    assert response_time < 1


def test_user_has_required_fields():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    for user in data:
        assert "name" in user
        assert "email" in user

        