from pizza import Pizza
from typing import Type
from enum import Enum
from topping_tuple import Topping

class Topping_names(Enum):
    PEPPERONI = "Pepperoni"
    MARGERITA = "Margerita"


class Main:
    def __init__(self, pizza: Type[Pizza], topping_maker: Type[Topping], topping_names: type[Topping_names]):
        self.current_pizza = Pizza("Blank")
        self.topping_maker = topping_maker
        self.topping_names = topping_names

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
            self.current_pizza = Pizza("Pepperoni", self.topping_maker(self.topping_names.PEPPERONI.value, 2), 
                                        self.topping_maker(self.topping_names.MARGERITA.value, 1))
            print("You have chosen Pepperoni!")

prices: dict[str, float] =  {}      
test = Main(Pizza, Topping, Topping_names)
test.selection()