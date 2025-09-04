from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from db import *


bot = Bot('7129279159:AAE-CpSY4mWh1mmJiLxpLcliP0vZpI-96z4')
dp = Dispatcher(bot, storage=MemoryStorage())


class AddQuestion(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()


class Question(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()


async def start(message: types.Message):
    user = userget(message.from_user.id)
    if user:
        await message.answer('Привет')
    else:
        useradd(message.from_user.id)
        await message.answer('Добро пожаловать')

async def admin(message: types.Message):
    text = message.text.split()
    if len (text) > 1:
        userpass = text[1]
        if userpass == 'qwerty123':
            addadmin(message.from_user.id)
            await message.answer('Выдача прав администратора')
        

async def startgame(message: types.Message):
    user = userget(message.from_user.id)
    if user[2] == 1:
        db_startgame()


async def stopgame(message: types.Message):
    user = userget(message.from_user.id)
    if user[2] == 1:
        db_stopgame()
        

async def quiestions(message: types.Message):
    user = userget(message.from_user.id)
    if user[2] == 1:
        delete_all_questions()
        await message.answer("Добавьте первый вопрос в формате\nТекст;вариант1;вариант2;вариант3;вариант4;правильный ответ")
        await AddQuestion.q1.set()


async def add_q1(message: types.Message, state: FSMContext):
    data = message.text.split(';')
    text = data[0]
    v1 = data[1]
    v2 = data[2]
    v3 = data[3]
    v4 = data[4]
    correct = data[5]
    add_question(text, v1, v2, v3, v4, correct)
    await message.answer("Добавьте второй вопрос в формате\nТекст;вариант1;вариант2;вариант3;вариант4;правильный ответ")
    await AddQuestion.q2.set()


async def add_q2(message: types.Message, state: FSMContext):
    data = message.text.split(';')
    text = data[0]
    v1 = data[1]
    v2 = data[2]
    v3 = data[3]
    v4 = data[4]
    correct = data[5]
    add_question(text, v1, v2, v3, v4, correct)
    await message.answer("Добавьте третий вопрос в формате\nТекст;вариант1;вариант2;вариант3;вариант4;правильный ответ")
    await AddQuestion.q3.set()


async def add_q3(message: types.Message, state: FSMContext):
    data = message.text.split(';')
    text = data[0]
    v1 = data[1]
    v2 = data[2]
    v3 = data[3]
    v4 = data[4]
    correct = data[5]
    add_question(text, v1, v2, v3, v4, correct)
    await message.answer("Ты молодец!")
    await state.finish()


async def game(message: types.Message, state: FSMContext):
    await message.answer('Игра началась')
    question = get_question(0)
    await state.update_data(correct=question[6])
    msg = f'Текст: {question[1]}\n{question[2]}\n{question[3]}\n{question[4]}\n{question[5]}'
    await message.answer(msg)
    await Question.q1.set()


async def q1(message: types.Message, state: FSMContext):
    correct = await state.get_data()
    if correct["correct"] == message.text:
        await message.answer("Ты молодец!")
    else:
        await message.answer("Могло быть и получше!")
    question = get_question(1)
    await state.update_data(correct=question[6])
    msg = f'Текст: {question[1]}\n{question[2]}\n{question[3]}\n{question[4]}\n{question[5]}'
    await message.answer(msg)
    await Question.q2.set()


async def q2(message: types.Message, state: FSMContext):
    correct = await state.get_data()
    if correct["correct"] == message.text:
        await message.answer("Ты молодец!")
    else:
        await message.answer("Могло быть и получше!")
    question = get_question(2)
    await state.update_data(correct=question[6])
    msg = f'Текст: {question[1]}\n{question[2]}\n{question[3]}\n{question[4]}\n{question[5]}'
    await message.answer(msg)
    await Question.q3.set()


async def q3(message: types.Message, state: FSMContext):
    correct = await state.get_data()
    if correct["correct"] == message.text:
        await message.answer("Ты молодец!")
    else:
        await message.answer("Могло быть и получше!")
    await message.answer("Игра завершилась")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(admin, commands='admin')
    dp.register_message_handler(startgame, commands= 'startgame')
    dp.register_message_handler(stopgame, commands= 'stopgame')
    dp.register_message_handler(quiestions, commands='questions')
    dp.register_message_handler(add_q1, state=AddQuestion.q1)
    dp.register_message_handler(add_q2, state=AddQuestion.q2)
    dp.register_message_handler(add_q3, state=AddQuestion.q3)
    dp.register_message_handler(game, commands='game')
    dp.register_message_handler(q1, state=Question.q1)
    dp.register_message_handler(q2, state=Question.q2)
    dp.register_message_handler(q3, state=Question.q3)
register_handlers(dp)



executor.start_polling(dp, skip_updates=True)