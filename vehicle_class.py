class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def what_car (self):
        return f"This {self.year} {self.model} from {self.make} is a total lemon!"
    
    def num_miles (self, miles):
        self.miles = miles
        return f'This {self.make} has {self.miles} on it. Good luck with your warrenty'

subaruin = Vehicle("Subaru", "Forester", 1999)

print(subaruin.what_car())
print(subaruin.num_miles(3000000))