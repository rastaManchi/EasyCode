from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Приветик)")

@dp.message_handler(commands="roll")
async def new(message):
    random_number = 0
    await message.answer(random_number)


executor.start_polling(dp, skip_updates=True)