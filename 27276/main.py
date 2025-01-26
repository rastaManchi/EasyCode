from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor


bot = Bot(token='7688359670:AAEf_gRt00OOD0Zil38X3LALoYE-F5ZupOA')
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def welcome(message):
    await message.answer('приветик)')

executor.start_polling(dp, skip_updates=True)
