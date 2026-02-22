import random
class Bank:
    def __init__(self, account_name, account_type, amount, ):
        self.account_name = account_name
        self.account_type = account_type
        self.amount = amount
       

class Account:
    def __init__(self):
        self.owner = []
        
        
    def create_account(self):
        account_name = input("Enter account name: ")
        account_type = input("1. Savings Account.\n2. Current Account\nChoose account type (1 or 2): ")
        amount = int(input("Enter initial deposit amount: "))
        bank = Bank(account_name, account_type, amount,)
        self.owner.append(bank)
        self.account_number = random.randint(10000000, 99999999)
        print(f"{account_name} added to bank list")
        
    def view_accounts(self):
      if not self.owner:
            print(f"{"~~" * 24}\n Account list is currently empty.\n{"~~" * 24}")
            return
      print("~~" * 32)

      for index, account in enumerate(self.owner):
       print(f"{index + 1}. Name: {account.account_name}, Account type: {account.account_type}, Account number: {self.account_number}, Balance: {account.amount}")
       
      print("~~" * 32)

    def deposit(self):
        account_name = input("Enter account name: ")
        amount = int(input("Enter deposit amount: "))
        for bank in self.owner:
            if bank.account_name == account_name:
                bank.amount += amount
                print(f"{amount} deposited into {account_name}")
                return
        

        print(f"{account_name} not found in bank list")

    def withdraw(self):
        account_name = input("Enter account name: ")
        amount = int(input("Enter withdrawal amount: "))
        for bank in self.owner:
            if bank.account_name == account_name:
                if bank.amount >= amount:
                    bank.amount -= amount
                    print(f"{amount} withdrawn from {account_name}")
                else:
                    print("Insufficient balance")
                return
            print(f"{account_name} not found in bank list")   

    def balance(self):
        account_name = input("Enter account name: ")

        for bank in self.owner:
            if bank.account_name == account_name:
                print(f"Current balance of {account_name} is {bank.amount}")
                return
            print(f"{account_name} not found in bank list")
    
    def run(self):
         while True:
            menu = input ("1. Create An Account.\n2. View Accounts.\n3. Deposit. \n4. Withdraw. \n5.  Check balance. \n6.  Exit. \nChoose an option(1|2|3|4|5|6):")
        
            match menu:
             case "1":
                self.create_account()
                print(self.owner)
             case "2":
                self.view_accounts()
             case "3":
                self.deposit()
             case "4":
                self.withdraw()
             case "5":
                self.balance()
             case "6":
                break
                

Account = Account()
Account.run()               