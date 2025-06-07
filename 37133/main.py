from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import aiogram.dispatcher.filters as filter
import random


bot = Bot(token='6735946626:AAFAkx8Vt8DR5u4UChIl0S444O7hHvWmhTc')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('message')


@dp.message_handler(filter.Text(equals=['Привет'], ignore_case=True))
async def first(message):
    await message.answer('И тебе привет)')


@dp.message_handler()
async def echo(message):
    text = message.text
    await message.answer(text)


@dp.message_handler(commands='Greetings')
async def Greetings(message):
    await message.answer('Здравствуй, мой Создатель, рад вас видеть!')

@dp.message_handler(commands='roll')
async def roll(message):
    await message.answer(random.randint(1,6))


@dp.message_handler(commands='credits')
async def credits(message):
    await message.answer('Бот создан Создателем Максима Заборщикова')
    await message.answer('telegram.@Makson2324')

executor.start_polling(dp, skip_updates=True)