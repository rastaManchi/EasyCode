from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message :types.Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True)