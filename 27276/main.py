from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor

from random import randint, choice
import os
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="token", parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

slides_file = open('slides.txt', 'r')
slides = slides_file.read().split('\n')
for i in range(len(slides)):
    slides[i] = slides[i].split(':')
slides_dict = {}
for slide in slides:
    slides_dict[slide[0]] = slide[1:]


class HandleClient(StatesGroup):
   waiting_for_slide = State()
   waiting_for_name = State()
   waiting_for_number = State()


async def start(message: types.Message):
    print(slides_dict)
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('КУПИТЬ БИЛЕТ')
    for slide in slides_dict:
        keyboard.add(slide)
    await message.answer('Добро пожаловать в аквапарк! Нажмите на название горки, чтобы получить больше информации, или на кнопку "купить билет", чтобы купить билет.', reply_markup=keyboard)
    await HandleClient.waiting_for_slide.set()
    

async def on_slide(message: types.Message):
    if message.text == 'КУПИТЬ БИЛЕТ':
        await message.answer('Стоимость билета - 2000 рублей на весь день. Чтобы купить билет, отправьте в чат своё имя:')
        await HandleClient.waiting_for_name.set()
    else:
        await message.answer(f'{message.text} - {slides_dict[message.text][1]}.\nПротяжённость горки - {slides_dict[message.text][0]} метров.')
        await message.answer_photo(types.InputFile(slides_dict[message.text][2]))


async def on_name(message: types.Message, state):
    await state.update_data(name=message.text)
    await message.answer('И номер телефона:')
    await HandleClient.waiting_for_number.set()


async def on_number(message: types.Message, state):
    await message.answer('Спасибо! Менеджер свяжется с вами для оплаты заказа.')
    data = await state.get_data()
    requests = open('requests.txt', 'a')
    requests.write(f'{data.get("name")} - {data.get("number")}')
    requests.close()
    await HandleClient.waiting_for_slide.set()


def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(on_slide, state=HandleClient.waiting_for_slide)
   dp.register_message_handler(on_name, state=HandleClient.waiting_for_name)
   dp.register_message_handler(on_number, state=HandleClient.waiting_for_number)

register_handlers(dp)

executor.start_polling(dp, skip_updates=True)