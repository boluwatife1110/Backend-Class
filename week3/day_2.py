import time
refreshments = [
    {"name": "rice", "unit_price": 1500},
    {"name": "smoothie", "unit_price": 1500},
    {"name": "gumea fowl", "unit_price": 12500},
    {"name": "yogurt", "unit_price": 5000},
    {"name": "fanta", "unit_price": 1000},
    {"name": "coke", "unit_price": 1000},
    {"name": "table water", "unit_price": 500},
    {"name": "chicken", "unit_price": 3500},
    {"name": "eba", "unit_price": 500},
    {"name": "eforiro", "unit_price": 1400},
    {"name": "pounded yam", "unit_price": 1000},
    {"name": "edikang ikong", "unit_price": 1200},
]
order =[]
def display_refreshments():
  for chow in refreshments:
    print(f"Name: {chow["name"]}, Price: {chow["unit_price"]}")

def search_for_refreshments(search_items):
      for chow in refreshments:
       if chow ["name"] == search_items:
        return chow
    
def run_program():
    print("Welcome to Eetables") # print this
    time.sleep(0.9) #Delay for 2 seconds

    display_refreshments()
    
    time.sleep (0.9)


    while True:
            query = input("what do you want to order?:")

            searched_refreshment = search_for_refreshments(search_items=query)
            # if searched_refreshment:
            #     print(f"Item '{query}' is available.")
            #     print(searched_refreshment)
            # else:
            #     print(f"Item '{query}' is not available.")
            if type(searched_refreshment) == dict:
             quantity= input(f"the price for {searched_refreshment["name"]}: is ₦{searched_refreshment["unit_price"]}. How many do you want?: ")

            price_per_quantity = searched_refreshment["unit_price"] * int(quantity)

            #add to order
            order.append({"name": searched_refreshment["name"],"quantity": int(quantity), "unit_price": price_per_quantity})

            choice_to_continue = input(f"You have added {searched_refreshment["name"]} with the price of ₦{price_per_quantity}. Do you want to continue ordering? (yes/no): ")
            if choice_to_continue == "yes":
             continue 
            elif choice_to_continue == "no":
             return 
            else:
            
             print("Invalid choice.")
    else:
            print(f"{query} is not in our menu.")

            

 
 

run_program()



