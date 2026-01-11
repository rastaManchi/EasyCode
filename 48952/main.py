import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode

from config import *


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart()) # /start
async def welcome(message):
    await message.answer('Привет!')
    
    
@dp.message(Command(commands='ЦРУ')) # /ЦРУ
async def test(message):
    await message.answer('И тебе ЦРУ!')
    

@dp.message(Command(commands='roll')) # /roll
async def roll(message):
    number = random.randint(1, 6)
    await message.answer(str(number))
    
    
@dp.message(F.text)
async def text_command(message):
    text = message.text
    if 'привет' in text.lower():
        await message.answer('`И тебе привет, меня зобут бот Криспер`', parse_mode=ParseMode.MARKDOWN_V2)


asyncio.run(dp.start_polling(bot))
