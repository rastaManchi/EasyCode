import asyncio
import random
import requests
import json
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import os

from config import *
from keyboards import *


bot = Bot(token=TOKEN)
dp = Dispatcher()
all_media_dir = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'all_media' )



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
    text = f"Температура сейчас: {temp}\nМинимальная температура: {temp_min}"
    await message.answer(text)  
    

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
    
    
@dp.message(Command(commands='send_photo'))
async def send_photo(message: Message):
    photo_file = FSInputFile(path=os.path.join(all_media_dir, 'mem.jpg'))
    await message.answer_photo(photo=photo_file)    


@dp.message(F.photo)
async def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    photo_file = await bot.get_file(photo_id)
    await bot.download_file(photo_file.file_path, os.path.join(all_media_dir, f"{photo_file.file_id}.jpg"))
    
    
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
    elif 'Звук' == text:
        sound_file = FSInputFile(path=os.path.join(all_media_dir, 'lucky-lucky.mp3'))
        await message.answer_audio(audio=sound_file, caption="Test")
    elif 'Голосовое' == text:
        voice_file = FSInputFile(path=os.path.join(all_media_dir, 'lucky-lucky.mp3'))
        await message.answer_voice(voice=voice_file, caption="Test")
    elif 'Группа фото' == text:
        photo1 = InputMediaPhoto(type='photo', 
                                 media=FSInputFile(os.path.join(all_media_dir, 'mem.jpg')),
                                 caption="Какой-то текст")
        photo2 = InputMediaPhoto(type='photo', media=FSInputFile(os.path.join(all_media_dir, 'mem2.jpg')))
        media = [photo1, photo2]
        await message.answer_media_group(media=media)


asyncio.run(dp.start_polling(bot))
