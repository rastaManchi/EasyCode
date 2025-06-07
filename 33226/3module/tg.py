from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from random import randint, choice
import os
import sqlite3


bot = Bot(token='7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw', parse_mode="HTML")
dp = Dispatcher(bot)


conn = sqlite3.connect('music.db')
cur = conn.cursor()


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
   item = cur.fetchone()
   await message.answer(f'Название: {item[0]}\nОписание: {item[2]}\nЦена: {item[1]}')


executor.start_polling(dp, skip_updates=True)