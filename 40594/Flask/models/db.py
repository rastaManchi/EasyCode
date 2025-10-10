from peewee import Model
from typing import List
from models.utils import db
from models.product import *
from datetime import datetime


def connection(function: callable):
    def wrapper(*args, **kwargs):
        with db.connection():
            res = function(*args, **kwargs)
            db.commit()
            return res
    return wrapper


@connection
def create_table(*models: Model):
    for model in models:
        if not model.table_exists():
            model.create_table()


@connection
def get_user(login, password) -> List[User]:
    return User.select().filter(gmail=login, password=password)


@connection
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

create_table(Item, Cart, User)

