import asyncio
import random
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
