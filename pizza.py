from topping_tuple import Topping

class Pizza:
    def __init__(self, name: str, *toppings: type[Topping]):
        self.name = name
        self.toppings = toppings
    
    def __str__(self):
        mylist: list[str] = []
        for topping in self.toppings:
            mylist.append(str(topping))
        return f"\nName: {self.name}\nToppings: {", ".join(mylist)}."
    
    def price_calc(self, price_change: float):
        self.price: int = 0
        for topping in self.toppings:
            self.price += topping.amount