from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command

import asyncio


bot = Bot(token="8236076703:AAFuYQCtw2YFgCnIhim7BUfwIDXCrWYCnDU")
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message):
    await message.answer("Привет")


@dp.message(Command(commands=["test"]))
async def test(message):
    await message.answer("tEST")



asyncio.run(dp.start_polling(bot))