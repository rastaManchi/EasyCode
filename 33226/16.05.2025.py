from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random
import requests
import json


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot, storage=MemoryStorage())


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
    else:
        for slide_name in slides_dict:
            if slide_name == name:
                await message.answer(slides_dict[slide_name])
                break



def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(command)

register_handlers(dp)


executor.start_polling(dp, skip_updates=True)