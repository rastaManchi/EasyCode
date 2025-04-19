from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
import random


bot = Bot(token="7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw")
dp = Dispatcher(bot)

films = {
   2022: {
       'Магия': ['Гарри Поттер 20 лет спустя', 'Тибра'],
       'Космос': ['Стражи Галактики: спецвыпуск', 'Падение луны'],
       'Комедия': ['Быстрее пули', 'Лулу и Бриггс']
   },
   2013: {
       'Магия': ['Хоббит: Пустошь Смауга', 'Охотники нв ведьм'],
       'Космос': ['СтарТрек: Возмездие', 'Риддик']
   },
   2008: {
       'Магия': ['Хроники Нарнии: Принц Каспиан', 'Гарри Поттер и Принц-полукровка'],
       'Космос': ['Звёздный Десант 3']
   }
}



@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Приветик)")

@dp.message_handler(commands="roll")
async def new(message):
    text = message.text
    spisok = text.split()
    if len(spisok) > 2:
        number_min = int(spisok[1])
        number_max = int(spisok[2])
        random_number = random.randint(number_min, number_max)
    elif len(spisok) == 2:
        number = int(spisok[1])
        random_number = random.randint(1, number)
    await message.answer(random_number)

@dp.message_handler(commands="films")
async def get_films(message):
    spisok = message.text.split()
    if len(spisok) >= 3:
        year = int(spisok[1])
        category = spisok[2]
        if year in films and category in films[year]:
            await message.answer('\n'.join(films[year][category]))
        elif not year in films:
            await message.answer('Нет фильмов этого года')
        elif not category in films[year]:
            await message.answer('Такой категории нет!')


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

@dp.message_handler(filters.Text(contains=['Привет'], ignore_case=True))
async def first(message :types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


executor.start_polling(dp, skip_updates=True)