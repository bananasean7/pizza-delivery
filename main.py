from pizza import Pizza
from typing import Type

class Main:
    def __init__(self, pizza: Type[Pizza]):
        self.current_pizza = Pizza("Blank")

    def selection(self):
        next_step = False
        while next_step == False:
            print()
            choice = input("""********************************
***Welcome to the Pizza Shop!***
***What would you like to do?***
***A: Order a pre built pizza***
***B: Print the current pizza***
Your Choice: """)
            choice = choice.upper()
            
            match choice:
                case "A":
                    self.pre_built()
                case "B":
                    print(self.current_pizza)
                case _:
                    pass
    
    def pre_built(self):
        print()
        pbchoice = input("""What type of pizza would you like: 
A: Pepperoni (Toppings: Pepperoni and Margerita)
Your choice: """)
        pbchoice = pbchoice.upper()

        if pbchoice == "A":
            self.current_pizza = Pizza("Pepperoni", "Pepperoni", "Margerita")
            print("You have chosen Pepperoni!")

        
test = Main(Pizza)
test.selection()