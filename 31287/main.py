import asyncio
from aiogram import Bot, Dispatcher, F, filters
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode

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
    
    
@dp.message(F.text)
async def text_command(message: Message):
    if message.text.lower() == 'привет':
        await message.answer('👍', parse_mode=ParseMode.MARKDOWN_V2)


asyncio.run(dp.start_polling(bot))