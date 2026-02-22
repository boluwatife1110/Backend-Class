# class Person:
#     type = "African"
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#      #Instance method: this method has self on it.
#     def speak(self):
#         return f"Hi, i'm {self.name}"
    
#     @classmethod
#     def common (cls):
#         return cls.type 
#     # static method: this method does not have self on it.
#     @staticmethod
#     def addition(a, b):
#         return a + b 
    
#     #Inbuilt method: this method is already built in python.
#     def __str__(self):
#         pass

#     def __repr__(self):
#         pass

#     def __eq__(self, value):
#         #logic
#         pass
      
    
# # king = Person("king")
# # print(king.common())

# #Inheritance: this is when a child class inherits from a parent class.
# # class Worker(Person):
# #     pass
# # paul = Worker(name="paul", age=42, gender="male")
# # print(paul.speak())
# class Worker(Person):
#     def __init__(self, name, age, gender, role, years_of_experience):
#         super().__init__(name, age, gender)
#         self.role = role
#         self.years_of_experience = years_of_experience


#       # Method Overiding
#     def speak(self):
#         return f"name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nRole: {self.role}\nYears of Experience: {self.years_of_experience}"
#      #Polymorphism: many forms
#     def join(self, a, b):
#         return a + b

# paul = Worker(name="paul", age=42, gender="male", role="software engineer", years_of_experience=5)

# print(paul.join(2, 4))
# print(paul.join("Woru ","Michael"))


#Encapsulation:this is when we hide the internal details of an object and only expose the necessary information to the outside world.
# Encapsulation : Hiding important data in a class
class ATM:
    def __init__(self) :
        self.__balance = 1000

    # Getter 
    def add_balance(self, amount):
        self.__balance = amount
        return self.__balance
    
    # Setter 
    def get_balance(self):
        return self.__balance
    
atm = ATM()
# print(atm.add_balance(2000))


class Engine:
    def start(self):
        return "Engine starting"
    
class Car():
    def __init__(self):
        self.engine = Engine() 

my_car = Car()
print(
    my_car.engine.start()
)