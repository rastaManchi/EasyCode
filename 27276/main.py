from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from random import randint, choice
import os
import sqlite3


conn = sqlite3.connect('27276/sql.db')
cur = conn.cursor()

bot = Bot(token='7688359670:AAEf_gRt00OOD0Zil38X3LALoYE-F5ZupOA', parse_mode="HTML")
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def meme(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    cur.execute('SELECT name FROM products')
    result = cur.fetchall()
    for item in result:
        keyboard.add(item[0])
    await message.answer('Добро пожаловать в магазин музыкальных товаров! Выберите товар ниже, чтобы узнать подробную информацию.', reply_markup=keyboard)


@dp.message_handler()
async def on_item(message: types.Message):
   cur.execute('SELECT name, price, description FROM products WHERE name = ?', [message.text])
   


executor.start_polling(dp, skip_updates=True)