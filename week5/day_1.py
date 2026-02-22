class Building:
    info = "This is a building"
    created_with = ["cement", "windows", "doors", "roof"]

    #Instance attribute
    def __init__(self, color, occupants, revenue):
        self.color = color
        self.occupants = occupants
        self.revenue = revenue

bank = Building("white", 55, "1 billion")
school = Building(color="red", occupants=241, revenue="100 million")


#Method
def run(self):
    return f"{self.name} is running with over {self.occupants} {"person" if self.occupants == 1 else "persons"} earing {self.revenue}"

bank = Building(name="vampay",color="white",occupants=55,revenue="1 billion")
school = Building(name="Sunshine Academy", color="cream_brown", occupants=241, revenue="100 million")

print(bank.run())
print(school.run())