class Cat:
    species = "mammal"
    legs = 4
    fur = 'long hair'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    #Instance Method
    def eat(self, cans_of_food):
        self.cans_of_food = cans_of_food
        return f"{self.name} ate {self.cans_of_food} cans of food"


guster = Cat("Guster", 10)

print(guster.name)
print(guster.eat(1))
print(Cat)