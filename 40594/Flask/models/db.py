from peewee import Model
from typing import List
from models.utils import db
from models.product import *
from datetime import datetime

def conection(function: callable):
    def wrapper(*args, **kwargs):
        with db.connection():
            res = function(*args, **kwargs)
            return res
    return wrapper
    
@conection
def create_table(*models: Model):
    for model in models:
        if not model.table_exists():
            model.create_table()

@conection
def get_user(login, password) -> List[User]:
    return User.select().filter(gmail=login, password=password)

@conection
def get_cart(user_id):
    cart = User.get(User.id == user_id).cart
    return cart


@conection
def get_cart_items(cart: Cart):
    response = []
    cartitems = CartItem.select().filter(cart=cart)
    for cartitem in cartitems:
        item = get_item(cartitem.item_id)
        response.append({
                'title': item.name,
                "quantity":1,
                "price":item.price,
                "image":"/static/media/бутсы.png",
                "id":item.id
            })
    return response

@conection
def add_cart_item(cart: Cart, item: Item):
    CartItem.create(cart=cart, item = item)

@conection
def create_item(name, desc, price, image):
    item = Item.create(name=name, desc=desc, price=price, image=image)
    return item

@conection
def get_item(item_id):
    item = Item.get(Item.id == item_id)
    return item


@conection
def create_user(login, password) -> List[User]:
    user = User.create(signUp_date=datetime.now(),
                last_signIn_date=datetime.now(),
                cookie_hash="",
                gmail=login,
                password=password,
                is_verified = False,
                cart = Cart.create(),
                name = login
                )
    return user

create_table(Item, Cart, User, CartItem)