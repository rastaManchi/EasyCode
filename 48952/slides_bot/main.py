import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
# TODO: импортировать классы для конечного автомата StatesGroup, State


from config import *
from keyboards import *


bot = Bot(token=TOKEN)
dp = Dispatcher()


# TODO: класс для конечного автомата


slides_file = open('slides.txt', 'r')
slides = slides_file.read().split('\n')
for i in range(len(slides)):
    slides[i] = slides[i].split(':')
slides_dict = {}
for slide in slides:
    slides_dict[slide[0]] = slide[1:]
    
    
@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer(START_MESSAGE, reply_markup=main_keyboard(slides_dict))
    
    
# TODO: обработать нажатие на кнопку КУПИТЬ БИЛЕТ
# TODO: написать функции ожидания имени и телефона пользователя
# TODO: сохранить данные в файл result.txt
    
    
asyncio.run(dp.start_polling(bot))