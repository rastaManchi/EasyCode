import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from helpers import *

bot = Bot(token='7129279159:AAE-CpSY4mWh1mmJiLxpLcliP0vZpI-96z4')
dp = Dispatcher(storage=MemoryStorage())





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())