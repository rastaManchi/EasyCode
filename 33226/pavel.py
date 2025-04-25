from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random

bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot, storage=MemoryStorage())

class HandleClient(StatesGroup):
   waiting_for_volume = State()
   waiting_for_gaz = State()
   waiting_for_address = State()


async def start(message, state):
   keyboard = types.ReplyKeyboardMarkup()
   keyboard.add('С кунжутом', 'Без кунжута')
   await message.answer('Привет! Я помогу тебе собрать бургер. Булочка с кунжутом или без кунжута?', reply_markup=keyboard)
   await HandleClient.waiting_for_volume.set()


async def on_volume(message, state):
   volume = message.text
   keyboard = types.ReplyKeyboardMarkup()
   keyboard.add('С луком', 'Без лука')
   await message.answer('Окей. С луком или без лука?', reply_markup=keyboard)
   await HandleClient.waiting_for_gaz.set()


async def on_gaz(message, state):
   gaz = message.text
   await message.answer('Отличный выбор! Куда доставить?')
   await HandleClient.waiting_for_address.set()


async def on_address(message, state):
   address = message.text
   await message.answer('Спасибо за заказ, обращайтесь! Привезём в течении часа.')
   await state.finish()


def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(on_volume, state=HandleClient.waiting_for_volume)
   dp.register_message_handler(on_gaz, state=HandleClient.waiting_for_gaz)
   dp.register_message_handler(on_address, state=HandleClient.waiting_for_address)

register_handlers(dp)


executor.start_polling(dp, skip_updates=True)