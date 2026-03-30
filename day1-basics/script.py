# GOAL 1
# Creating a function that: takes a list of users (dict);  filters only active users; returns their emails

# 1. List of the users {"name": "Anna", "email": "...", "is_active": True/False}
users = [
    {"name": "Anna", "email": "anna@example.com", "is_active": True},
    {"name": "John", "email": "john@example.com", "is_active": False},
    {"name": "Maria", "email": "maria@example.com", "is_active": True},
    {"name": "Tom", "email": "tom@example.com", "is_active": False}
]

# 2. Function - get active users from the list

def get_active_user_emails(users):
    active_emails = []

# 3. For loop - filter all the list in order to get just active users
    for user in users:
        if user["is_active"] == True:
            active_emails.append(user["email"])

    return active_emails


# 4. Starting the function
result_active = get_active_user_emails(users)
print(result_active)

# GOAL 2
# Creating a function that: takes a list of users (dict);  filters only users with domain example.com; returns their names and emails

# 1. Function - get users with example.com domain from the list

def get_users_with_example_domain(users):
    example_domain = []

# 2. For loop - filter all the list in order to get users with domain example.com
    for user in users:
        if "example.com" in user["email"]: 
            example_domain.append({"name": user["name"], "email": user["email"]})

    return example_domain

# 3. Starting the function
result_domain = get_users_with_example_domain(users)
print(result_domain)
