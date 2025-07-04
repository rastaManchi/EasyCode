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


async def welcome(message: types.Message):
    user_id = message.from_user.id
    user_from_db = get_user(user_id)
    if not user_from_db:
        add_user(user_id)
    await message.answer('И тебе не хворать')


async def game(message: types.Message):
    await message.answer('Привет')
    question = get_all_questions()[0]
    await message.answer(f'{question[1]}\n\n{question[2]}\n\n{question[3]}\n\n{question[4]}\n\n{question[5]}')
    await Question.ans1.set()


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
    dp.register_message_handler(q1, state=Question.ans1)
    dp.register_message_handler(q2, state=Question.ans2)
    dp.register_message_handler(q3, state=Question.ans3)
    dp.register_message_handler(q4, state=Question.ans4)
    dp.register_message_handler(q5, state=Question.ans5)


register_handlers(dp)


executor.start_polling(dp, skip_updates=True)
