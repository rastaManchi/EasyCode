import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message

from config import *
from keyboards import *


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart()) # /start
async def welcome(message):
    await message.answer('Привет!', reply_markup=main_keyboard())
    
    
@dp.message(Command(commands='ЦРУ')) # /ЦРУ
async def test(message):
    await message.answer('И тебе ЦРУ!')
    

@dp.message(Command(commands='roll')) # /roll
async def roll(message):
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
        await message.answer(f'name: {name}\nis_premium\: {is_premium}\nusername: {username}', reply_markup=inline_keyboard())


asyncio.run(dp.start_polling(bot))
