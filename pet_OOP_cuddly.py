from pet_OOP import Pet
class CuddlyPet(Pet):
    def __init__(self, name, fullness = 50, happiness = 150, hunger = 10, mopiness = 5, extra_sweet = 0):
        super().__init__(name, fullness, 100, hunger, 5)
        self.extra_sweet = extra_sweet
        pass
    def cuddle(self, other_pet):
        other_pet.get_love()
    def __str__(self):
        return "This pet is extra cuddly."
    def be_alive(self, wigglyness):
        super().be_alive()
        #self.wigglyness = wigglyness
        #self.happiness -= self.mopiness / 2
        self.extra_sweet += 5

benji = CuddlyPet("Benji")
cujo = Pet("Cujo")

benji.cuddle(cujo)
print(benji)

print(cujo.happiness)

