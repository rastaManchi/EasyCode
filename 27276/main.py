from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from random import randint, choice
import os
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='7688359670:AAEf_gRt00OOD0Zil38X3LALoYE-F5ZupOA', parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


class HandleClient(StatesGroup):
   waiting_for_slide = State()
   waiting_for_name = State()
   waiting_for_number = State()


async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('КУПИТЬ БИЛЕТ')
    # ... 
    slides = [] # ...
    for slide in slides:
        keyboard.add(slide[0])
    await message.answer('Добро пожаловать в аквапарк! Нажмите на название горки, чтобы получить больше информации, или на кнопку "купить билет", чтобы купить билет.', reply_markup=keyboard)
    await HandleClient.waiting_for_slide.set()
    

async def on_slide(message: types.Message):
    if message.text == 'КУПИТЬ БИЛЕТ':
        await message.answer('Стоимость билета - 2000 рублей на весь день. Чтобы купить билет, отправьте в чат своё имя:')
        await HandleClient.waiting_for_name.set()
    else:
        pass
        # ...
        # await message.answer(f'{message.text} - {slide[1]}.\nПротяжённость горки - {slide[0]} метров.')


async def on_name(message: types.Message, state):
    await state.update_data(name=message.text)
    await message.answer('И номер телефона:')
    await HandleClient.waiting_for_number.set()


async def on_number(message: types.Message, state):
    await message.answer('Спасибо! Менеджер свяжется с вами для оплаты заказа.')
    data = await state.get_data()
    # ...
    await HandleClient.waiting_for_slide.set()


def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(on_slide, state=HandleClient.waiting_for_slide)
   dp.register_message_handler(on_name, state=HandleClient.waiting_for_name)
   dp.register_message_handler(on_number, state=HandleClient.waiting_for_number)

register_handlers(dp)

executor.start_polling(dp, skip_updates=True)
