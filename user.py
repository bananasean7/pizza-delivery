import json
from typing import Type

class User:
    def __init__(self, uname: str, pword: str, number_of_orders: int= 0, money_spent: float = 0):
        self.uname = uname
        self.pword = pword
        self.number_of_orders = number_of_orders
        self.money_spent = money_spent
    
    def __str__(self):
        return f"Hello {self.uname}!.\nYou have placed {self.number_of_orders} orders and have spent €{self.money_spent}"

class Database:
    def __init__(self, file: str, user: Type[User]):
        self.file = file
        self.db: dict[str, tuple[str, int, float]] = dict()
        self.user = user
    
    def dump(self, data): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        with open(self.file, "w") as f:
            json.dump(data, f)
    
    def view(self):
        with open(self.file, "r") as f:
            foo = json.load(f)
            self.db = foo
            return foo
    
    def new_user(self, new_name: str, new_pword: str):
        self.db = self.view()
        self.db[new_name] = [new_pword, 0, 0] # pyright: ignore[reportArgumentType]
        self.dump(self.db) # pyright: ignore[reportUnknownMemberType]
    
    def login(self, uname: str):
        self.view()
        if uname in self.db.keys():
            pword = input(f"Enter password {uname}: ")
            if str(pword) == self.db[uname][0]:
                return self.user(uname, *self.db[uname])
    
    def update(self, user: User):
        with open(self.file, "w") as f:
            self.db[user] = [user.pword, user.money_spent, user.number_of_orders]
            json.dump(self.db, f)

if __name__ == "__main__":
    db = Database("user_database.json", User)
    db.new_user("larry", "boop")
    x = db.login("larry")
    print(x)