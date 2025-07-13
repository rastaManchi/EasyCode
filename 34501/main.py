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


class Buy(StatesGroup):
    name = State()
    phone = State()




# Хендлеры
@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    slides = ReplyKeyboardBuilder()
    slides.button(text = 'buy ticket')
    slides_db = get_all_slides()
    for slide in slides_db:
        slides.button(text=slide[1])
    await message.answer(
        'Добро пожаловать в аквапарк! Нажмите на название горки, чтобы получить больше информации, '
        'или на кнопку "КУПИТЬ БИЛЕТ", чтобы купить билет.',reply_markup=slides.as_markup(rezise_keydoard=True))


@dp.message(F.text, Buy.name)
async def name_waiting(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Приятно познакомиться, введите ваш номер телефона: ')
    await state.set_state(Buy.phone)
    
    
@dp.message(F.text, Buy.phone)
async def phone_waiting(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer('Ваши данные переданы менеджеру!')
    data = await state.get_data()
    await bot.send_message(190203478, f'Имя: {data.get("name")}\nТелефон: {data.get("phone")}')
    await state.clear()


@dp.message(F.text)
async def about(message: Message, state: FSMContext):
    if message.text == 'buy ticket':
        await message.answer('Цена билета 2000р, введите свое имя: ')
        await state.set_state(Buy.name)
    else:
        slide = get_slide_by_name(message.text)
        if slide:
            await message.answer(f"Название горки: {message.text}\nПротяженность:{slide[2]}м\n{slide[3]}")
        else:
            await message.answer('Такой горки нет!')


# Основная функция запуска
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())