from peewee import Model, PrimaryKeyField, TextField, CharField, BooleanField, ForeignKeyField, DateTimeField, ManyToManyField, IntegerField, FloatField
from models.utils import db


class Item(Model):
    id = PrimaryKeyField()
    name = CharField()
    desc = TextField()
    price = FloatField()
    image = TextField()

    class Meta:
        database = db


class Cart(Model):
    id = PrimaryKeyField()
    items = ManyToManyField(Item, backref="item")

    class Meta:
        database = db


class User(Model):
    id = PrimaryKeyField()
    signUp_date = DateTimeField()
    last_signIn_date = DateTimeField()
    cookie_hash = TextField()
    gmail = TextField()
    password = TextField()
    is_verified = BooleanField()
    cart = ForeignKeyField(Cart)
    name = CharField()

    class Meta:
        database = db