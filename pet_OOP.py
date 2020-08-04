from pet_OOP_treat import Treat
class Pet:
    def __init__(self, name, fullness=100, happiness=100, hunger = 5, mopiness = 5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness


    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    
    def __str__ (self):
        return f"{self.name} is {self.fullness} full and {self.happiness} happy"
    
    def be_alive (self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
    
    def give_treat(self, treat_type):
        self.happiness += treat_type.add_happiness()
        self.fullness += treat_type.add_fullness()
        

    


