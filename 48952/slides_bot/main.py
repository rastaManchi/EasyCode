import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import *
from keyboards import *
from db import *


bot = Bot(token=TOKEN)
dp = Dispatcher()


class Anceta(StatesGroup):
    name = State()
    phone = State()


slides_file = open('slides.txt', 'r', encoding='utf-8')
slides = slides_file.read().split('\n')
for i in range(len(slides)):
    slides[i] = slides[i].split(':')
slides_dict = {}
for slide in slides:
    slides_dict[slide[0]] = slide[1:]
    
print(slides_dict)
    
    
@dp.message(CommandStart())
async def welcome(message: Message):
    if add_user(message.from_user.id,
             message.from_user.username,
             message.from_user.first_name,
             message.from_user.last_name,
             "-1"):
        await message.answer("Добро пожаловать!", reply_markup=main_keyboard(slides_dict))
    await message.answer(START_MESSAGE, reply_markup=main_keyboard(slides_dict))
    

@dp.message(Anceta.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Введите номер телефона')
    await state.set_state(Anceta.phone)
    

@dp.message(Anceta.phone)
async def get_city(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(phone=phone)
    await message.answer('Спасибо за уделенное время!')
    data = await state.get_data()
    text = f"Имя: {data['name']} -- Телефон: {data['phone']}\n"
    await message.answer(text)
    
    # 3. TODO: воспользоваться функцией add_ticket(name, phone, message.from_user.id)
    
    file = open('result.txt', 'a', encoding='utf-8')
    file.write(text)
    file.close()
    await state.clear()


@dp.message(F.text)
async def commands(message: Message, state: FSMContext):
    text = message.text
    if text == 'КУПИТЬ БИЛЕТ':
        await message.answer('Как вас зовут?')
        await state.set_state(Anceta.name)
    else:
        if text in slides_dict:
            await message.answer(f"Название: {text}\nДлина горки: {slides_dict[text][0]}\nОписание: {slides_dict[text][1]}")

    
    
asyncio.run(dp.start_polling(bot))