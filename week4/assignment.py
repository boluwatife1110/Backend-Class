# ====================== BACKEND THINKING FUNCTIONS ASSIGNMENT ======================
# Topic: Backend Logic, API Responses, User Validation, Real Practice


# 1. Write a function called login_user(username, password)
#    - If username is "admin" and password is "1234"
#      return "Login Successful"
#    - Else return "Invalid Credentials"
# Answer no 1 here.
def login_user(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"
print(login_user("admin", "1234"))
print(login_user("bolu", "3243"))

# 2. Write a function called response(message, code)
#    It should return a dictionary like:
#    {"status": code, "message": message}
# Answer no 2 here.
def response(message, code):
    return {"status": code, "message": message}
check = response("Success", 200)
print(check)


# 3. Write a function called validate_username(name)
#    Return True if the username has at least 4 characters,
#    else return False.
# Answer no 3 here.

def validate_username(name):
     return len(name) >= 4
print(validate_username("Mike")) 
print(validate_username("Sam"))   


# 4. Write a function called is_valid_email(email)
#    Return True if email contains "@" and "."
#    Else return False.
# Answer no 4 here.
def validate_email(email):
    if "@" in email:
        return True
    else:
        return False
print(validate_email("michael@gmail.com")) 
print(validate_email("michaelgmail.com")) 


def get_user_by_id(users, id):
    for user in users:
        if user["id"] == id:
            return user
    

users = [
    {"id": 1, "name": "Mike"},
    {"id": 2, "name": "Sarah"},
    {"id": 3, "name": "John"}
]

print(get_user_by_id(users, 2))





# 6. Write a function called calculate_order_total(order)
#    order is a list like:
#    [{"item": "rice", "price": 2000}, {"item": "beans", "price": 3000}]
#    Return the total cost.
# Answer no 6 here.


# 7. Write a function called add_product(products, name, price)
#    It should add a new dictionary into the products list:
#    {"name": name, "price": price}
# Answer no 7 here.


# 8. Write a function called check_permission(role)
#    - If role is "admin" return "Full Access"
#    - If role is "user" return "Limited Access"
#    - Else return "No Access"
# Answer no 8 here.


# 9. Write a function called update_profile(user_dict, **changes)
#    It should update the dictionary with the new values
#    and return the updated dictionary.
# Answer no 9 here.


# 10. Given a list of users with active status,
#     write a function called count_active_users(users)
#     Return how many users are active (True).
# Answer no 10 here.
def count_active_users(users):
    count = 0
    for user in users:
        if user["active"] == True:
            count += 1
    return count

users = [
    {"id": 1, "name": "Mike", "active": True},
    {"id": 2, "name": "Sarah", "active": False},
    {"id": 3, "name": "John", "active": True}
]

print(count_active_users(users))

