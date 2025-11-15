from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import asyncio

from config import *
from keyboards import *


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Привет", reply_markup=await main_keyboard())


@dp.message(Command(commands=["test"]))
async def test(message: Message):
    await message.answer("tEST")


@dp.message(F.text)
async def text_command(message: Message):
    if message.text == "Профиль":
        await message.answer(str(message.from_user.id), reply_markup=await test_inline())
    elif message.text == "Пока":
        await message.answer("И тебе пока")


@dp.callback_query()
async def check_inline_btn(call):
    if call.data == "test_btn":
        print("На кнопку нажали!")

asyncio.run(dp.start_polling(bot))