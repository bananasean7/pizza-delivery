from pizza import Pizza
from typing import Type
from enum import Enum
from topping_tuple import Topping
from user import Database, User
from time import sleep

class Topping_names(Enum):
    PEPPERONI = Topping("Pepperoni", 0.5)
    MARGERITA = Topping("Margerita", 0.25)
    SALAMI = Topping("Salami", 0.25)
    SAUSAGE = Topping("Sausage", 0.35)


class Main:
    def __init__(self, pizza: Type[Pizza], topping_maker: Type[Topping], topping_names: type[Topping_names], database: Type[Database]):
        self.topping_maker = topping_maker
        self.topping_names = topping_names
        self.current_pizza = Pizza("Blank", topping_names.MARGERITA.value)
        self.current_user: User = None # pyright: ignore[reportAttributeAccessIssue]
        self.db = database("user_database.json", User)

    def selection(self):
        next_step: bool = False
        while next_step == False:
            print()
            choice = input("""********************************
***Welcome to the Pizza Shop!***
***What would you like to do?***
***A: Order a pre built pizza***
***B: Print the current pizza***
***C: Proceed to the next step***
Your Choice: """)
            choice = choice.upper()
            
            match choice:
                case "A":
                    self.pre_built()
                case "B":
                    print(self.current_pizza)
                case "C":
                    next_step = True
                case _:
                    pass
        
        self.pay_for_pizza()

    def pre_built(self):
        print()
        pbchoice = input("""What type of pizza would you like: 
A: Pepperoni (Toppings: Pepperoni and Margerita)
B: Meat Feast (Toppings: Margerita, Salami and Sausage)
C: Double Cheese (Toppings: x2 Margerita)
Your choice: """)
        pbchoice = pbchoice.upper()

        if pbchoice == "A":
            self.current_pizza = Pizza("Pepperoni", self.topping_names.PEPPERONI.value, self.topping_names.MARGERITA.value)
            print("You have chosen Pepperoni!")
        if pbchoice == "B":
            self.current_pizza = Pizza("Meat Feast", self.topping_names.MARGERITA.value, 
                                       self.topping_names.SALAMI.value, self.topping_names.SAUSAGE.value)
            print("You have chosen Meat Feast!")
        if pbchoice == "C":
            self.current_pizza = Pizza("Double Cheese", self.topping_names.MARGERITA.value, self.topping_names.MARGERITA.value)
            print("You have chosen Double Cheese!")
        
        self.price(0.75, 1)

    def price(self, low_change: float, med_change: float):
        print(f"Your {self.current_pizza.name} will cost {self.current_pizza.price_calc(low_change)} with a or {self.current_pizza.price_calc(med_change)} without a discount")
        discount_code: str = input("Enter discount code or leave blank if no discount code: ")

        if discount_code == "6767":
            self.current_pizza.price = self.current_pizza.price_calc(0.75) # pyright: ignore[reportAttributeAccessIssue]
        else:
            self.current_pizza.price = self.current_pizza.price_calc(1) # pyright: ignore[reportAttributeAccessIssue]
        
    def pay_for_pizza(self):
        next_step: bool = False
        while next_step == False:
            print("You must login to pay for your pizza!")
            account_exists: str = input("Does you already have an account?\n(Y/N)")
            
            if account_exists.upper() == "Y":
                uname = input("What was the account username: ")
                self.current_user = self.db.login(uname) # pyright: ignore[reportAttributeAccessIssue]
                if self.current_user != None: # pyright: ignore[reportUnnecessaryComparison]
                    self.current_user.money_spent += self.current_pizza.price
                    self.current_user.number_of_orders += 1
                    
                    print("Your pizza has been ordered!")
                    print("Please wait 5 minutes to receive litterally nothing")
                    sleep(300)
                    print("Welp that was a waste of time")
            
            if account_exists.upper() == "N":
                print("An account will be created")
                new_name = input("Enter new name: ")
                new_pword = input("Enter your new password: ")
                print(f"Creating new account with username {new_name} and {new_pword}")
                self.current_user = self.db.new_user(new_name, new_pword) # pyright: ignore[reportAttributeAccessIssue]
        
        print(self.current_user)
    
  
test = Main(Pizza, Topping, Topping_names, Database)
test.selection()