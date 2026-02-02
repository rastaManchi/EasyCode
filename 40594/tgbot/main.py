from config import *
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer('Привет, я крутой бот')
    
    
@dp.message(Command(commands='info'))
async def info(message: Message):
    await message.answer('Я - бот')


asyncio.run(dp.start_polling(bot))