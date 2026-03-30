import requests

# --- GET REQUEST ---
def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    
    print("GET status:", response.status_code)
    return response.json()


# --- DATA FILTERING ---
def get_emails(users):
    return [user["email"] for user in users]


# --- POST REQUEST ---
def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "QA test", "body": "API test", "userId": 1}
    
    response = requests.post(url, json=payload)
    
    print("POST status:", response.status_code)
    print("Response:", response.json())


# --- MAIN FLOW ---
users = get_users()

emails = get_emails(users)
print("Emails:", emails)

create_post()


# --- GET emails with biz---
def get_emails_biz(users):
    return [user["email"] for user in users if "biz" in user ["email"]]