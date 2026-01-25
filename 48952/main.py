import asyncio
import random
import requests
import json
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import *
from keyboards import *


bot = Bot(token=TOKEN)
dp = Dispatcher()


class Anceta(StatesGroup):
    name = State()
    age = State()
    city = State()


@dp.message(CommandStart()) # /start
async def welcome(message: Message):
    await message.answer('Привет!', reply_markup=main_keyboard())


@dp.message(Command(commands='ЦРУ')) # /ЦРУ
async def test(message: Message, state: FSMContext):
    await message.answer('И тебе ЦРУ!')
    await message.answer('Как тебя зовут?')
    await state.set_state(Anceta.name)
    

@dp.message(Command(commands='weather')) # /weather city
async def weather(message: Message):
    city = message.text.split()[1]
    r = requests.get(FIND_LAT_LON_URL.replace('city', city).replace('apikey', WEATHER_API))
    data = json.loads(r.content)
    lat = str(data[0]['lat'])
    lon = str(data[0]['lon'])
    r = requests.get(GET_WEATHER_URL.replace('{lat}', lat).replace('{lon}', lon).replace('apikey', WEATHER_API))
    data = json.loads(r.content)
    temp = round(data['main']['temp'] - 273, 0)
    temp_min = "10"
    text = f"Температура сейчас: {temp}\nМинимвльная темература: {temp_min}"
    # TODO: добавить temp_feel, max_temp, min_temp, wind_speed, wind_deg
    # TODO: ответить пользователю красивым сообщением
    
    await message.answer(text)
    
    
"""
{
  "coord": {
    "lon": 127.5272,
    "lat": 50.2905
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 255.49,
    "feels_like": 248.49,
    "temp_min": 255.49,
    "temp_max": 255.49,
    "pressure": 1031,
    "humidity": 46,
    "sea_level": 1031,
    "grnd_level": 1008
  },
  "visibility": 10000,
  "wind": {
    "speed": 3,
    "deg": 280
  },
  "clouds": {
    "all": 0
  },
  "dt": 1769335256,
  "sys": {
    "type": 1,
    "id": 8859,
    "country": "RU",
    "sunrise": 1769296458,
    "sunset": 1769328575
  },
  "timezone": 32400,
  "id": 2026609,
  "name": "Blagoveshchensk",
  "cod": 200
}
"""
    
    

@dp.message(Anceta.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Сколько тебе лет?')
    await state.set_state(Anceta.age)
    

@dp.message(Anceta.age)
async def get_age(message: Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.answer('Из какого вы города?')
    await state.set_state(Anceta.city)
    

@dp.message(Anceta.city)
async def get_city(message: Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer('Спасибо за уделенное время!')
    data = await state.get_data()
    text = f"Имя: {data['name']} -- Возраст: {data['age']} -- Город: {data['city']}\n"
    await message.answer(text)
    file = open('new.txt', 'a', encoding='utf-8')
    file.write(text)
    file.close()
    await state.clear()
    

@dp.message(Command(commands='roll')) # /roll
async def roll(message: Message):
    number = random.randint(1, 6)
    await message.answer(str(number))
    
    
@dp.message(F.text)
async def text_command(message: Message):
    text = message.text
    if 'привет' in text.lower():
        await message.answer('`И тебе привет, меня зобут бот Криспер`', parse_mode=ParseMode.MARKDOWN_V2)
    elif 'Профиль' == text:
        name = message.from_user.first_name
        id = message.from_user.id
        is_premium = message.from_user.is_premium
        username = message.from_user.username
        await message.answer(f"id: `{id}`", )
        await message.answer(f'name: {name}\nis_premium\: {is_premium}\nusername: {username}')


asyncio.run(dp.start_polling(bot))
