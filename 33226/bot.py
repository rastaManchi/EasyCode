from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Приветик)")

@dp.message_handler(commands="roll")
async def new(message):
    random_number = 0
    await message.answer(random_number)


# {
#  "message_id": 5, 
#  "from": {
#      "id": 190203478,
#      "is_bot": false,
#      "first_name": "Булат",
#      "username": "rastabubblegum",
#      "language_code": "ru",
#      "is_premium": true
#      },
#  "chat": {
#          "id": 190203478,
#          "first_name": "Булат",
#          "username": "rastabubblegum",
#          "type": "private"},
#  "date": 1744395973,
#  "text": "123123"
# }

@dp.message_handler(filters.Text(equals=['Привет'], ignore_case=True))
async def first(message :types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


executor.start_polling(dp, skip_updates=True)