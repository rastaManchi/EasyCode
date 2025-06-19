from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random


bot = Bot(token='6735946626:AAFAkx8Vt8DR5u4UChIl0S444O7hHvWmhTc')
dp = Dispatcher(bot, storage=MemoryStorage())


class HandleClient(StatesGroup):
   waiting_for_volume = State()
   waiting_for_gaz = State()
   waiting_for_address = State()

async def start(message, state):
   await message.answer('Привет! Здесь можно заказать воду. Сколько литров привезти?')
   await HandleClient.waiting_for_volume.set()

async def on_volume(message, state):
   volume = message.text
   await state.update_data(kolvo=volume)
   keyboard = types.ReplyKeyboardMarkup()
   keyboard.add('Газированная', 'Негазированная')
   await message.answer('Окей. Вода должна бать газированной или негазированной?', reply_markup=keyboard)
   await HandleClient.waiting_for_gaz.set()

async def on_gaz(message, state):
   gaz = message.text
   await state.update_data(gaznegaz=gaz)
   await message.answer('Отличный выбор! Куда доставить?')
   await HandleClient.waiting_for_address.set()

async def on_address(message, state):
   address = message.text
   await state.update_data(vashaddress=address)
   await message.answer('Спасибо за заказ, обращайтесь! Привезём через пол часа.')
   data = await state.get_data()
   await message.answer(f'{data.get("kolvo")}Л\n{data.get("gaznegaz")}\n{data.get("vashaddress")}')
   await state.finish() 

def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(on_volume, state=HandleClient.waiting_for_volume)
   dp.register_message_handler(on_gaz, state=HandleClient.waiting_for_gaz)
   dp.register_message_handler(on_address, state=HandleClient.waiting_for_address)

register_handlers(dp)

executor.start_polling(dp, skip_updates=True)