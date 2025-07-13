import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from helpers import *
bot = Bot(token='6943333150:AAGA-uXOML1M88KaLtslNoXzF46eJZm7yxU')
dp = Dispatcher(storage=MemoryStorage())





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


@dp.message(F.text)
async def about(message: Message):
    slide = get_slide_by_name(message.text)
    print(slide)


# Основная функция запуска
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())