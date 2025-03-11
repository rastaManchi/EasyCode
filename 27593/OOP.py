class Item:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def addToCart(self, i:Item):
        self.items.append(i)
        self.total += i.price

class User:
    def __init__(self, id, name, balance, cart:Cart):
        self.id = id
        self.name = name
        self.balance = balance
        self.cart = cart

    def buy(self):
        if self.balance >= self.cart.total:
            self.balance -= self.cart.total
            self.cart.items = []
            return True
        return False


apple = Item(1, 'Яблоко', 'Описание', 100)

u1 = User(1, 'Булат', 50, Cart())
u1.cart.addToCart(apple)
print(u1.buy(), u1.balance)

