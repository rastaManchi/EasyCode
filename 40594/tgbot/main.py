from config import *
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import asyncio
from keyboards import *


class Anceta(StatesGroup):
    name = State()
    age = State()
    phone = State()


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer('Привет, я крутой бот', reply_markup=contact_keyboard())
    
    
@dp.message(Command(commands='info'))
async def info(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя: ')
    await state.set_state(Anceta.name)


@dp.message(Anceta.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Сколько вам лет?')
    await state.set_state(Anceta.age)


@dp.message(Anceta.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите номер телефона?', reply_markup=contact_keyboard())
    await state.set_state(Anceta.phone)
    
    
@dp.message(Anceta.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data() # {"name": "", "age": "", "phone": ""}
    await message.answer('Спасибо за участие!')
    print(data)
    await state.clear()
    

@dp.message(F.text)
async def text_commands(message: Message):
    pass


@dp.callback_query()
async def inline_commands(call: CallbackQuery):
    if call.data == 'test':
        await call.message.delete()
    


asyncio.run(dp.start_polling(bot))