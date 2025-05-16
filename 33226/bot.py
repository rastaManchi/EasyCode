from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random
import requests
import json

bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot, storage=MemoryStorage())

admin = 190203478

class HandleClient(StatesGroup):
   waiting_for_volume = State()
   waiting_for_gaz = State()
   waiting_for_address = State()



async def start(message: types.Message, state: FSMContext):
   print(message.chat.id)
   if not message.from_user.first_name and not message.from_user.last_name:
      await message.answer('Здравствуйте!')
   else:
      result = ''
      if message.from_user.first_name:
         result += message.from_user.first_name
      if message.from_user.last_name:
         result += f' {message.from_user.last_name}'
      await message.answer(f'Здравствуйте, {result}')
   await message.answer('Привет! Здесь можно заказать воду. Сколько литров привезти?')
   await HandleClient.waiting_for_volume.set()


async def on_volume(message: types.Message, state: FSMContext):

   volume = message.text
   await state.update_data(volume=volume)
   keyboard = types.ReplyKeyboardMarkup()
   keyboard.add('Газированная', 'Негазированная')
   await message.answer('Окей. Вода должна бать газированной или негазированной?', reply_markup=keyboard)
   await HandleClient.waiting_for_gaz.set()


async def on_gaz(message: types.Message, state: FSMContext):
   gaz = message.text
   await state.update_data(gaz=gaz)
   await message.answer('Отличный выбор! Куда доставить?')
   await HandleClient.waiting_for_address.set()


async def on_address(message: types.Message, state: FSMContext):
   address = message.text
   await state.update_data(address=address)
   await message.answer('Спасибо за заказ, обращайтесь! Привезём через пол часа.')
   data = await state.get_data()
   await message.answer(f'{data.get("volume")} | {data.get("gaz")} | {data.get("address")}')
   await bot.send_message(admin, f'{data.get("volume")} | {data.get("gaz")} | {data.get("address")}')
   await state.finish()


async def get_photo(message: types.Message):
   # media = types.MediaGroup()
   # media.attach_photo(types.InputFile("33226/41-run-head.png"))
   # media.attach_photo(types.InputFile("33226/41-run-head.png"))
   # media.attach_photo(types.InputFile("33226/41-run-head.png"))
   # await bot.send_media_group(message.chat.id, media=media) # только для bot.send_media_group
   r = requests.get('https://dog.ceo/api/breeds/image/random')
   data = json.loads(r.content)
   url = data["message"]
   print(url)
   await message.answer(url)

   # await message.answer_photo(types.InputFile("33226/41-run-head.png"))



async def sent_photo(message: types.Message):
   print(message.photo[-1])
   await message.photo[-1].download()
   


def register_handlers(dp: Dispatcher):
   dp.register_message_handler(start, commands="start")
   dp.register_message_handler(get_photo, commands="get_photo")
   dp.register_message_handler(sent_photo, content_types=['photo'])
   dp.register_message_handler(on_volume, state=HandleClient.waiting_for_volume)
   dp.register_message_handler(on_gaz, state=HandleClient.waiting_for_gaz)
   dp.register_message_handler(on_address, state=HandleClient.waiting_for_address)

register_handlers(dp)


executor.start_polling(dp, skip_updates=True)