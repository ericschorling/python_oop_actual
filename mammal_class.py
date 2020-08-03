class Mammal:
    def __init__(self, type_of_mammal, breed, legs, name):
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs
        self.name = name

    def eat(self): 
        return f"The {self.name} is eating.!"

class Cat(Mammal):
    def __init__(self, type_of_mammal, breed, legs, name, fur):
        super().__init__(type_of_mammal,breed,legs, name)
        self.fur = fur
    def __str__ (self):
        return f"{self.name} is a {self.type_of_mammal} with {self.legs} legs and really nice {self.fur} fur"

    def eat(self):
        return "The cat won't eat anything."


guster = Cat("cat", "mixed", 4, "Gus","short hair")
harry = Mammal("dog", "shit-poo", 5, "Johnny")
print(guster)
print(guster.eat())
print(harry.eat())

