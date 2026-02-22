# # # Functions 
# # '''
# # A function is a block of codes that performs a specific task

# # Benefits of using functions:
# # 1. it helps to perform specific task.
# # 2. Organization.
# # 3. Reusability.
# # '''

# from unicodedata import name


# def name_of_function():
#     #statement in here
#     return
# def addition():
#     num = 1
#     another_num = 2
#     add = num + another_num
#     return add
# print(

# addition ()
# )


# def subtraction():
#     num_1 = 5
#     num_2 = 2
#     sub = num_1 - num_2

#     return sub
# print(
#     subtraction()
# )


# def multiplicaion():
#     num_1 = 5
#     num_2 = 2
#     multply = num_1 * num_2

#     return multply
# print(
#     multiplicaion()
# )


# # # parameters and arguments

# def user(name):
#     return name 
# print(
#     user ("King")
# )
# print(
#     user ("Bolex")
# )

# def user (name, age, country):
#     return name, age, country
# print(
#     user("Bolu", 11, "Nigeria")
# )


# #examples with functions
# def check_students_age(age):
#     if age <=15:
#         return "you are eligible to apply for this scholarship."
#     else:
#         return "you are not eligible to apply for this scholarship."
    
    
# print (
#        "student A",
#        check_students_age(13)
#      )
# print (
#        "student B",
#        check_students_age(17)
#      )

# def check_students_age(age):
#     age = age ** 2
#     return age
# print ( 
#     check_students_age(int(input("Enter your age:")))
# )

# def user (name, age, country):
#     return {"name": name, "age": age, "country": country}
# user1 = user("Boluwatife", "11", "Nigeria")


# print(
#     user1["name"] 
# )


# # Arguments
# # types of arguments
# # 1. positional arguments
# #2. keyword arguments

def user (name, age , country):
    return name, age, country

user2 = user (name="Bolu", country="Nigeria", age="11")

print(
    user2
)
#Default arguments
def game (mode= "Easy"):
    return mode

run_game = game ("Hard")

print(run_game)

# 4. ARGS - variable length arguments
def guest (*info):
    return info
run_guest = guest("King", "Boluwatife", "Male", "Vip")
print(run_guest)

# 5. KWARGS - Keyword as an argument
def another_guest (**info):
    return info

print()

def car(details):
    return details
print(
    car("tesla")
)

def car(**details):
    return details
new_car = car(color= "black", model= "2025", make = "Tesla")
print(new_car)