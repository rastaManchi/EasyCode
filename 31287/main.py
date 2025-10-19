import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import warnings, logging
from datetime import datetime

warnings.filterwarnings("ignore")
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.INFO)


bot = Bot(token="8236076703:AAFuYQCtw2YFgCnIhim7BUfwIDXCrWYCnDU")
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message):
    await message.answer("Привет")
    logging.info(f"[{datetime.now()}] Тест")


@dp.message(Command(commands="test")) # /test
async def test(message: Message):
    await message.answer("Test")


asyncio.run(dp.start_polling(bot))