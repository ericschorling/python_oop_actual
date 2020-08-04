#from pet_OOP import Pet
class Treat():
    def __init__(self, treat="",  add_happy=0, add_full=0, cost = 0):
        self.treat = treat
        self.add_happy = add_happy
        self.add_full = add_full
        self.cost = cost
    
    def add_happiness(self):
        return self.add_happy
    def add_fullness(self):
        return self.add_full
    def pay_for_it(self,num):
        return self.cost * num
    def __str__(self):
        return "There are 3 types of treat. Which would you like to give?\n1. Cold Pizzia \n 2. Bacon \n 3. Vegan Snack\n"
    def return_info(self):
        return f"{self.treat} will give {self.add_happy} happiness and {self.add_full} fullness.\n It costs ${self.cost}"

class ColdPizza(Treat):
    def __init__(self, treat="", add_happy=0, add_full =0, cost = 0):
        super().__init__("Cold Pizza", 3, 10, 2)
   
class Bacon(Treat):
    def __init__(self, treat, add_happy=0, add_full=0, cost = 0):
        super().__init__(treat,10,3,2)
    