
import random
#import pet_OOP
from garden_classes import Garden
from garden_classes import Tree
from garden_classes import Gnome
from garden_classes import Woodchuck

global turn_counter

def main():
    turn_counter = 0
    new_garden = Garden("Secret Garden")
    
    new_garden.add_trees("Tree")
    new_garden.add_gnomes("Gnome")
    new_garden.add_woodchuck("Woodchuck")
    
    while True:
        rain_or_chuck = random.randint(1,100)
        if rain_or_chuck < 20:
            print("It rained today.")
            new_garden.water_level(5)
        elif rain_or_chuck >90:
            print("Damn another woodchuck moved in!")
        else:
            print(f"Another beautiful day in the {new_garden.name}")



        print(new_garden)
        turn_counter += 1

main()
