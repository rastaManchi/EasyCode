from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random
import requests
import json

import sqlite3


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot, storage=MemoryStorage())

conn = sqlite3.connect('33226/slides.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS slides(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            length INTEGER,
            description TEXT
            )''')
conn.commit()

class BuyTicket(StatesGroup):
    name = State()
    tel = State()
    date = State()


file = open('33226/slides.txt', 'r', encoding='utf-8')
slides = file.read().split('\n')
slides_dict = {}
for slide in slides:
    slide_info = slide.split(':')
    slides_dict[slide_info[0]] = slide_info[1:]


async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add("КУПИТЬ БИЛЕТ")
    for slide_name in slides_dict:
        keyboard.add(slide_name)
    await message.answer('Приветик', reply_markup=keyboard)


async def command(message: types.Message):
    name = message.text
    if name == 'КУПИТЬ БИЛЕТ':
        await message.answer('Круто, как тебя зовут?')
        await BuyTicket.name.set()
    else:
        for slide_name in slides_dict:
            if slide_name == name:
                await message.answer(slides_dict[slide_name])
                break


async def name(message: types.Message, state: FSMContext):
    user_name = message.text
    await state.update_data(username=user_name)
    await message.answer('Зафискировали, а теперь введите ваш телефон: ')
    await BuyTicket.tel.set()


async def tel(message: types.Message, state: FSMContext):
    usertel = message.text
    await state.update_data(usertel=usertel)
    await message.answer('Круто, теперь дата: ')
    await BuyTicket.date.set()

#{'username': 'Булат', 'usertel': '123424234', 'userdate': '12.06'}

async def date(message: types.Message, state: FSMContext):
    userdate = message.text
    await state.update_data(userdate=userdate)
    data = await state.get_data()
    file = open('33226/requests.txt', 'a', encoding='utf-8')
    file.write(f'{data["username"]} -- {data["usertel"]} -- {data["userdate"]}')
    file.close()
    await message.answer('Увидимся!')
    await state.finish()


def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(command)
   dp.register_message_handler(name, state=BuyTicket.name)
   dp.register_message_handler(tel, state=BuyTicket.tel)
   dp.register_message_handler(date, state=BuyTicket.date)

register_handlers(dp)


executor.start_polling(dp, skip_updates=True)