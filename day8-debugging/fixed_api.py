import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(f"{BASE_URL}/users")


def get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    return response.json()


def create_user():
    payload = {
        "name": "John Doe",
        "email": "john@example.com"
    }

    return requests.post(f"{BASE_URL}/users", json=payload)
