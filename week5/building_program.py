import time
import random

class Company:
    info = "This is a company"

    def __init__(self, company_name, founded):
        self.company_name = company_name
        self.founded = founded
        self.revenue = 0
        self.staff = []


    def operate(self):
        options = ["loss", "mid_profit", "high_profit"]
        random_option = random.choice(options)  
        print(random_option)
       

        if random_option == "loss":
            revenue = self.revenue - 500
        elif random_option == "mid_profit":
            revenue = self.revenue + 1000
        elif random_option == "high_profit":
            revenue = self.revenue + 2000
     
        
        self.revenue = revenue
        print(self.revenue)

    def run_program(self):
        self.operate()

vampay = Company("vampay", "2026")
vampay.run_program()
