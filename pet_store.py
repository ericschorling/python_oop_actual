from pet_OOP import Pet
from pet_OOP_treat import Treat
from pet_OOP_treat import ColdPizza

def main():
    generic_treat = Treat('generic')
    cold_pizza = ColdPizza()
    benji = Pet('benji')
    print("Welcome to the Pet Store. You have many options for taking care of your pet.")

    user_input = input("would you like to give your pet a treat?")
    

    #if user_input.upper() != 'Y' or user_input.upper() != 'N':
     #   print("Please use the correct option")
    if user_input.upper() == 'Y':
        user_input = int(input(generic_treat))
    else:
        print("guess they will go hungry...")
    
    if user_input == 1:
        benji.give_treat(cold_pizza)
        print(cold_pizza.return_info())
    #elif: user_input ==
     #   benji.give_treat(cold_pizza)

    print(benji)

    #benji.give_treat(bacon_treat)

main()