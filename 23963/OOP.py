class Item:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.id} - {self.name} - {self.description} - {self.price}'
    

class Inventory:
    def __init__(self):
        self.max_items = 10
        self.items = []


class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def addToCart(self, item:Item):
        self.items.append(item)
        self.total += item.price


class User:
    def __init__(self, id, name, balance, cart:Cart, inventory:Inventory):
        self.id = id
        self.name = name
        self.balance = balance
        self.cart = cart
        self.inventory = inventory

    def buy(self):
        if self.balance >= self.cart.total:
            self.balance -= self.cart.total
            if len(self.cart.items) + len(self.inventory.items) > self.inventory.max_items:
                print('Количество товаров превышено!')
                return False
            for item in self.cart.items:
                self.inventory.items.append(item)
                self.cart.items.remove(item)
                print('ok')
                return True
        return False
        
    def show_cart(self):
        for item in self.cart.items:
            print(item)
        

i1 = Item(0, 'Тест', 'Тест', 10000)
i2 = Item(1, 'Новый', 'Описание', 100)

c1 = Cart()
inv1 = Inventory()
u1 = User(0, 'Булат', 100000000000000000, c1, inv1)

u1.cart.addToCart(i1)
u1.buy()

for i in range(9):
    u1.cart.addToCart(i1)

u1.show_cart()

u1.buy()


