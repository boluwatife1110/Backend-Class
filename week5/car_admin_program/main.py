class Car:
    def __init__(self, name, model, year_of_manufacture, color):
        self.name = name
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.color = color
class Main:
   def __init__(self):
      self.list_of_cars = []


   def add_car(self):
      name = input("Enter the name of the car: ")
      model = input("Enter the model of the car: ")
      year_of_manufacture = input("Enter the year of manufacture of the car: ")
      color = input("Enter the color of the car: ")
      car = Car(name, model, year_of_manufacture, color)
      self.list_of_cars.append(car)
      print(f"{name} added to car list")


   def view_cars(self):
      if not self.list_of_cars:
            print(f"{"~~" * 24}\n There are no cars in the list.\n{"~~" * 24}")
            return
      print("~~" * 32)

      for index, car in enumerate(self.list_of_cars):
         print(f"{index + 1}. name: {car.name}, model: {car.model}, year of manufacture: {car.year_of_manufacture}, color: {car.color}")
       
      print("~~" * 32)

   def delete_a_car(self):
      #list the cars with index
    while True:
       self.view_cars()
       index = input("what car do you want to delete?(write a number):")

       # solve the validation rule yourself

       self.list_of_cars.pop(int(index)- 1)
       print("car removed out of the list.")
       break
   
   def run(self):
        while True:
            menu = input ("1. Add a car.\n2. View all cars. \n3. Delete a car. \n4. Exit. \nChoose an option(1|2|3|4):")
        
            match menu:
             case "1":
                self.add_car()
                print(self.list_of_cars)
             case "2":
                self.view_cars()
             case "3":
                self.delete_a_car()
             case "4":
                break
main = Main()
main.run()