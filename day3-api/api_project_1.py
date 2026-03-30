# -- GOAL: Get users (GET), Extract specific data, Check conditions (manual tests in the code), Send a POST, Verify the response --

import requests

# --- CONFIG ---
BASE_URL = "https://jsonplaceholder.typicode.com"


# --- GET USERS ---
def get_users():
    response = requests.get(f"{BASE_URL}/users")
    
    assert response.status_code == 200, "GET /users failed"
    
    return response.json()


# --- FILTER USERS ---
def get_active_like_users(users):
    # (email includes 'biz')
    return [user for user in users if "biz" in user["email"]]


# --- EXTRACT EMAILS ---
def get_emails(users):
    return [user["email"] for user in users]


# --- POST REQUEST ---
def create_post():
    payload = {
        "title": "QA Automation Test 1",
        "body": "Testing API",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201, "POST failed"

    data = response.json()

    # validation
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    return data


# --- MAIN FLOW ---
def main():
    users = get_users()

    print("Total users:", len(users))

    filtered_users = get_active_like_users(users)
    print("Filtered users:", len(filtered_users))

    emails = get_emails(filtered_users)
    print("Emails:", emails)

    post = create_post()
    print("Created post:", post)


if __name__ == "__main__":
    main()