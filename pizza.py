from topping_tuple import Topping
from collections import Counter

class Pizza:
    def __init__(self, name: str, *toppings: Topping):
        self.name = name
        self.toppings = Counter(toppings)
        self.price = 0
    
    def __str__(self):
        mylist: list[str] = []
        for topping in self.toppings.elements():
            mylist.append(f"€{topping.price} {topping.name}")
        return f"\nName: {self.name}\nToppings: {", ".join(mylist)}.\nPrice: €{self.price}"
    
    def price_calc(self, price_change: float):
        price: float = 0
        for topping in self.toppings.elements():
            price += topping.price
        return price * price_change