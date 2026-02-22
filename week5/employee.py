import time

class Employees:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, gender, role):
        self.employees.append({"name": name, "age": age, "gender": gender, "role": role})
        return 
    
    def run_employee_program(self):
        while True:
                print("Add an employee")
                time.sleep(0.9)
                name = input("Name of employees: ")
                age = input("Age of employees: ")
                gender = input("Gender of employees: ")
                role = input("Role of employees: ")


                self.add_employee(name, age, gender, role)
                time.sleep(0.9)

                print(f"Employee added. \nTotal employees:  {len(self.employees)}")
                option = input("do you want to continue?(y/n):")
                if option == "y":
                    continue
                elif option == "n":
                    break
                else:
                    break

employees = Employees()

employees.run_employee_program()