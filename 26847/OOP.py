class Item:
    def __init__(self, id, name, description, price):
        self.id = id 
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name


# Создайте класс Cart для интернет-магазина с полями:
# Список товаров
# Общая стоимость покупки
# И методом addToCart, который примет на выход объект Item, добавит его в список товаров и увеличит итоговую стоимость.

class Cart:
    def __init__(self):
        self.items = []
        self.total = 1000
   
    def addToCart(self, item):
        self.items.append(item)
        self.total += item.price

    def show_items(self):
        items = ''
        for item in self.items:
            items += f'{item.name}\n'
        return items


# Создайте класс User для интернет-магазина с полями:
# id
# Имя
# Баланс
# Корзина
# И методом buy. Метод должен:
# Вычитать из баланса сумму покупки при условии, что денег у пользователя достаточно
# Возвращать True, если баланса для покупки хватило и False, если не хватило


class User:
    def __init__(self, id, name, balance, cart: Cart):
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
    
    def __str__(self):
        return f'{self.name} -- {self.balance} -- {self.cart.show_items()}'
    
u1 = User(1, 'Булат', 1500, Cart())
u2 = User(2, 'Андрей', 19, Cart())
banana = Item(1, 'Банан', 'вкусный', 200)
u1.cart.addToCart(banana)
u1.cart.addToCart(banana)
u1.cart.addToCart(banana)
u2.cart.addToCart(banana)
print(u1.buy())
print(u1)
print(u2)



