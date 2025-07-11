from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from sql import *


bot = Bot(token='7642230007:AAHSxCKstV2WJVzsygPsoTINbpMj7eyYmJw') 
dp = Dispatcher(bot, storage=MemoryStorage())


class Question(StatesGroup):
    ans1 = State()
    ans2 = State()
    ans3 = State()
    ans4 = State()
    ans5 = State()
    
    
class AddQuestion(StatesGroup):
    ans1 = State()
    ans2 = State()
    ans3 = State()
    ans4 = State()
    ans5 = State()


async def welcome(message: types.Message):
    user_id = message.from_user.id
    user_from_db = get_user(user_id)
    if not user_from_db:
        add_user(user_id)
    await message.answer('И тебе не хворать')


async def admin(message: types.Message):
    text = message.text
    l = len(text.split())
    if l > 1:
        password = text.split()[1]
        if password == 'qwerty':
            set_admin(message.from_user.id)


async def startgame(message: types.Message):
    user = get_user(message.from_user.id)
    if user[2] == 1:
        db_startgame()
        users = get_all_user()
        for user in users:
            await bot.send_message(user[1], 'Игра началась!')
        
    
async def stopgame(message: types.Message):
    user = get_user(message.from_user.id)
    if user[2] == 1:
        db_stopgame()
        users = get_all_user()
        for user in users:
            await bot.send_message(user[1], 'Игра закончилась!')
    


async def questions(message: types.Message):
    user = get_user(message.from_user.id)
    if user[2] == 1:
        delete_questions()
        await message.answer('Добавьте новый вопрос <text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        await AddQuestion.ans1.set()
    else:
        await message.answer('Вы не являетесь администартором!')


async def a1(message: types.Message, state: FSMContext):
    question = message.text.split(';')
    if len(question) == 6:
        text = question[0]
        q1 = question[1]
        q2 = question[2]
        q3 = question[3]
        q4 = question[4]
        correct = question[5]
        add_new_question(text, q1, q2, q3, q4, correct)
        await message.answer('Добавьте новый вопрос <text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        await AddQuestion.ans2.set()
    else:
        await message.answer('Неправильно введены данные!\n<text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        

async def a2(message: types.Message, state: FSMContext):
    question = message.text.split(';')
    if len(question) == 6:
        text = question[0]
        q1 = question[1]
        q2 = question[2]
        q3 = question[3]
        q4 = question[4]
        correct = question[5]
        add_new_question(text, q1, q2, q3, q4, correct)
        await message.answer('Добавьте новый вопрос <text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        await AddQuestion.ans3.set()
    else:
        await message.answer('Неправильно введены данные!\n<text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')

async def a3(message: types.Message, state: FSMContext):
    question = message.text.split(';')
    if len(question) == 6:
        text = question[0]
        q1 = question[1]
        q2 = question[2]
        q3 = question[3]
        q4 = question[4]
        correct = question[5]
        add_new_question(text, q1, q2, q3, q4, correct)
        await message.answer('Добавьте новый вопрос <text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        await AddQuestion.ans4.set()
    else:
        await message.answer('Неправильно введены данные!\n<text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')

async def a4(message: types.Message, state: FSMContext):
    question = message.text.split(';')
    if len(question) == 6:
        text = question[0]
        q1 = question[1]
        q2 = question[2]
        q3 = question[3]
        q4 = question[4]
        correct = question[5]
        add_new_question(text, q1, q2, q3, q4, correct)
        await message.answer('Добавьте новый вопрос <text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')
        await AddQuestion.ans5.set()
    else:
        await message.answer('Неправильно введены данные!\n<text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')

async def a5(message: types.Message, state: FSMContext):
    question = message.text.split(';')
    if len(question) == 6:
        text = question[0]
        q1 = question[1]
        q2 = question[2]
        q3 = question[3]
        q4 = question[4]
        correct = question[5]
        add_new_question(text, q1, q2, q3, q4, correct)
        await message.answer('Процесс добавлеения вопросов завершен!')
        await state.finish()
    else:
        await message.answer('Неправильно введены данные!\n<text; вариант1; вариант2; вариант3; вариант4; правильный ответ>')


async def game(message: types.Message):
    if get_status():
        await message.answer('Привет')
        question = get_all_questions()[0]
        await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
        await Question.ans1.set()
    else:
        await message.answer('Игра еще не началась!')


async def q1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text)
    await message.answer('Круто')
    question = get_all_questions()[1]
    await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
    await Question.ans2.set()
    
async def q2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text)
    await message.answer('Круто')
    question = get_all_questions()[2]
    await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
    await Question.ans3.set()

async def q3(message: types.Message, state: FSMContext):
    await state.update_data(q3=message.text)
    await message.answer('Круто')
    question = get_all_questions()[3]
    await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
    await Question.ans4.set()
    
async def q4(message: types.Message, state: FSMContext):
    await state.update_data(q4=message.text)
    await message.answer('Круто')
    question = get_all_questions()[4]
    await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
    await Question.ans5.set()
    
async def q5(message: types.Message, state: FSMContext):
    await state.update_data(q5=message.text)
    data = await state.get_data()
    print(data)
    await message.answer('Круто')
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome, commands='start')
    dp.register_message_handler(game, commands='game')
    dp.register_message_handler(admin, commands='admin')
    dp.register_message_handler(questions, commands='questions')
    dp.register_message_handler(startgame, commands='startgame')
    dp.register_message_handler(stopgame, commands='stopgame')
    dp.register_message_handler(q1, state=Question.ans1)
    dp.register_message_handler(q2, state=Question.ans2)
    dp.register_message_handler(q3, state=Question.ans3)
    dp.register_message_handler(q4, state=Question.ans4)
    dp.register_message_handler(q5, state=Question.ans5)
    dp.register_message_handler(a1, state=AddQuestion.ans1)
    dp.register_message_handler(a2, state=AddQuestion.ans2)
    dp.register_message_handler(a3, state=AddQuestion.ans3)
    dp.register_message_handler(a4, state=AddQuestion.ans4)
    dp.register_message_handler(a5, state=AddQuestion.ans5)


register_handlers(dp)


executor.start_polling(dp, skip_updates=True)
