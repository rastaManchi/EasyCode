from config import *
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import asyncio


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer('Привет, я крутой бот')
    
    
@dp.message(Command(commands='info'))
async def info(message: Message):
    await message.answer('Я - бот')
    

@dp.message(F.text)
async def text_commands(message: Message):
    pass


@dp.callback_query()
async def inline_commands(call: CallbackQuery):
    if call.data == 'test':
        await call.message.delete()
    


asyncio.run(dp.start_polling(bot))