# ============================================================
# Week 4
# FUNCTIONS ASSIGNMENT (Backend Developer Practice)
# Topic: Functions, Parameters, Return Values, *args, **kwargs
# Instructions:
# - Answer each question by writing a function.
# - Call your function to test it.
# ============================================================


# 1. Write a function called greet_user() that returns:
#    "Welcome to the Backend Class!"
# Answer no 1 here.
def greet_user():
    return "Welcome to the Backend Class!"
print(
    greet_user()
)

# 2. Write a function called add_numbers(a, b) that returns the sum of two numbers.
# Answer no 2 here.
def add_numbers():
    a = 17
    b= 11
    sum = a + b
    return sum
print(
    add_numbers()
)

# 3. Write a function called subtract_numbers(a, b) that returns the difference.
# Answer no 3 here.
def subtract_numbers():
    a = 17
    b = 11
    sub = a - b
    return sub
print(
    subtract_numbers()
)


# 4. Write a function called format_full_name(first_name, last_name)
#    that returns: "Full Name: John Doe"
# Answer no 4 here.
def format_full_name ( first_name, last_name):
    return first_name , last_name
full_name = format_full_name ( first_name = "John" , last_name = "Doe")
print(
    full_name
)


# 5. Write a function called check_login(is_logged_in)
#    If True return "Access Granted"
#    Else return "Access Denied"
# Answer no 5 here.
def check_login(is_logged_in):
    if is_logged_in:
        return "Access Granted"
    else:
        return "Access Denied"
print(check_login(True))



# 6. Write a function called student_profile(name, age, course)
#    that returns a dictionary with the student information.
# Answer no 6 here.
def student_profile(name, age, course):
    return {
        "name": name,
        "age": age,
        "course": course
    }
studentA = student_profile("Michael", 20, "Computer Science")
studentB = student_profile("Andi", 25, "Computer Science")
studentC = student_profile("Vicky", 25, "English")

print(studentA, studentB, studentC)



# 7. Write a function called is_adult(age)
#    Return "Adult" if age >= 18 else "Minor"
# Answer no 7 here.
def is_adult():
    age = int(input("How old are you? "))

    if age >= 18:
        return "Adult."
    else:
        return "Minor."

print(
    is_adult()
      )


# 8. Write a function called calculate_discount(price, discount=10)
#    Apply the discount percentage and return the final price.
# Answer no 8 here.
def calculate_discount(price=100, discount=10):
    final_price = price - (price * discount / 100)
    return final_price
print(calculate_discount())  


# 9. Write a function called register_users(*names)
#    It should return all names inside a tuple.
# Answer no 9 here.
def register_users(*names):
    return names
names = register_users("Michael", "Andi", "Victoria")
print(
    names
)

# 10. Write a function called create_account(**details)
#     It should return the details as a dictionary.
# Answer no 10 here.
def create_account(**details):
    return details
account = create_account(name="Michael", age=20, email="michael@gmail.com")
print(
    account
    )



# 11. Write a function called backend_response(message, status="success")
#     Return:
#     {"status": status, "message": message}
# Answer no 11 here.
def backend_response(message, status="success"):
    return {"status": status, "message": message}
print(
    backend_response("Account created successfully")
    )


# 12. Write a function called find_product(products, name)
#     products will be a list of dictionaries.
#     Return the dictionary that matches the product name.
# Answer no 12 here.
def find_product(products, name):
    for product in products:
        if product.get("name") == name:
            return product
        else: 
         return None  
products = [
    {"name": "rice"},
    {"name": "beans"},
    {"name": "oil"}
]

print(find_product(products, "beans"))
print(find_product(products, "sugar"))



# 13. Write a function called total_cart_price(cart)
#     cart is a list of items like:
#     {"name": "rice", "price": 2000}
#     Return the total price.
# Answer no 13 here.
def total_cart_price(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total
cart = [
    {"name": "rice", "price": 2000},
    {"name": "beans", "price": 1500},
    {"name": "oil", "price": 2500}
]

print(
    total_cart_price(cart)
    )  



# 14. Write a function called add_to_cart(cart, item_name, quantity, unit_price)
#     It should add a new dictionary into the cart list.
# Answer no 14 here.
def add_to_cart(cart, item_name, quantity, unit_price):
    # Create a new item dictionary
    item = {
        "item_name": item_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": quantity * unit_price
    }
    cart.append(item)
    return cart
cart = []

add_to_cart(cart, "Rice", 2, 5000)
add_to_cart(cart, "Beans", 3, 3000)

print(cart)



# 15. Write a function called generate_receipt(cart)
#     Print each item and return the total cost.
# Answer no 15 here.




# ============================================================
# BONUS (Real Backend Thinking)
# ============================================================

# 16. Write a function called validate_email(email)
#     Return True if email contains "@" else False.
# Answer no 16 here.
def validate_email(email):
    if "@" in email:
        return True
    else:
        return False
print(validate_email("michael@gmail.com")) 

# 17. Write a function called api_response(data, code=200)
#     Return:
#     {"code": code, "data": data}
# Answer no 17 here.
def api_response(data, code=200):
    return {"code": code,"data": data}
print(
    api_response(data={"name": "Michael"})
    )

# 18. Write a function called update_user(user_dict, **kwargs)
#     Update the user dictionary with new values.
# Answer no 18 here.
def update_user(user_dict, **kwargs):
    for key, value in kwargs.items():
        user_dict[key] = value
    return user_dict


print(
    update_user({"name": "Boluwatife"}, age=14, gender="male")
)


# 19. Write a function called find_max_number(numbers)
#     numbers is a list of integers.
#     Return the largest number in the list.
# Answer no 19 here.
def find_max_number(numers):
    return max(numers)
numbers = (1, 2, 4, 7, 88, 100, 14, 44)
print(
   max(numbers)
)

# 20. Write a function called count_vowels(word)
#     Return the number of vowels (a, e, i, o, u) in the word.
# Answer no 20 here.
def count_vowels(word):
  count = 0

  for character in word:
      if character in "aeiou":
          count = count + 1
  else:
      return count
  
print(
    count_vowels("Favour")
)
