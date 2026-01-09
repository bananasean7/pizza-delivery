class Pizza:
    def __init__(self, name: str, *toppings: str):
        self.name = name
        self.toppings= toppings
    
    def __str__(self):
        return f"\nName: {self.name}\nToppings: {", ".join(self.toppings)}."
    
    def price_calc(self, price_change: float):
        self.price: float = len(self.toppings) * price_change
