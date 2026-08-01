import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(f"{BASE_URL}/users")


def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")


def create_user():
    payload = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    return requests.post(f"{BASE_URL}/users", json=payload)


def update_user_put(user_id):
    payload = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    return requests.put(f"{BASE_URL}/users/{user_id}", json=payload)


def update_user_patch(user_id):
    payload = {
        "name": "Patched Name"
    }
    return requests.patch(f"{BASE_URL}/users/{user_id}", json=payload)


def delete_user(user_id):
    return requests.delete(f"{BASE_URL}/users/{user_id}")
