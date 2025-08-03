import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command, CommandStart
from helpers import *

bot = Bot(token='6943333150:AAGA-uXOML1M88KaLtslNoXzF46eJZm7yxU')
dp = Dispatcher(storage=MemoryStorage())


class AddQuestion(StatesGroup):
    a1 = State()
    a2 = State()
    a3 = State()
    a4 = State()
    a5 = State()


@dp.message(CommandStart())
async def hello(message: Message):
    await message.answer('Привет')
    user = get_user_by_id(message.from_user.id)
    if not user:
        add_user(message.from_user.id)


@dp.message(Command('admin'))
async def admin(message: Message):
    text_split = message.text.split()
    if len(text_split) > 1:
        password = text_split[1]
        if password == '1234':
            add_admin(message.from_user.id)
            

@dp.message(F.text, AddQuestion.a1)
async def a1_waiting(message: Message, state: FSMContext):
    text_split = message.text.split(';')
    text_question = text_split[0]
    ans1 = text_split[1]
    ans2 = text_split[2]
    ans3 = text_split[3]
    ans4 = text_split[4]
    correct = text_split[5]
    add_question(text_question, ans1, ans2, ans3, ans4, correct)
    await message.answer("Вопрос добавлен, продолжайте:\nTEXT;ans1;ans2;ans3;ans4;correct")
    await state.set_state(AddQuestion.a2)
    

@dp.message(F.text, AddQuestion.a2)
async def a1_waiting(message: Message, state: FSMContext):
    text_split = message.text.split(';')
    text_question = text_split[0]
    ans1 = text_split[1]
    ans2 = text_split[2]
    ans3 = text_split[3]
    ans4 = text_split[4]
    correct = text_split[5]
    add_question(text_question, ans1, ans2, ans3, ans4, correct)
    await message.answer("Вопрос добавлен, продолжайте:\nTEXT;ans1;ans2;ans3;ans4;correct")
    await state.set_state(AddQuestion.a3)
    
    
@dp.message(F.text, AddQuestion.a3)
async def a1_waiting(message: Message, state: FSMContext):
    text_split = message.text.split(';')
    text_question = text_split[0]
    ans1 = text_split[1]
    ans2 = text_split[2]
    ans3 = text_split[3]
    ans4 = text_split[4]
    correct = text_split[5]
    add_question(text_question, ans1, ans2, ans3, ans4, correct)
    await message.answer("Вопрос добавлен, продолжайте:\nTEXT;ans1;ans2;ans3;ans4;correct")
    await state.set_state(AddQuestion.a4)


@dp.message(F.text, AddQuestion.a4)
async def a1_waiting(message: Message, state: FSMContext):
    text_split = message.text.split(';')
    text_question = text_split[0]
    ans1 = text_split[1]
    ans2 = text_split[2]
    ans3 = text_split[3]
    ans4 = text_split[4]
    correct = text_split[5]
    add_question(text_question, ans1, ans2, ans3, ans4, correct)
    await message.answer("Вопрос добавлен, продолжайте:\nTEXT;ans1;ans2;ans3;ans4;correct")
    await state.set_state(AddQuestion.a5)
    

@dp.message(F.text, AddQuestion.a5)
async def a1_waiting(message: Message, state: FSMContext):
    text_split = message.text.split(';')
    text_question = text_split[0]
    ans1 = text_split[1]
    ans2 = text_split[2]
    ans3 = text_split[3]
    ans4 = text_split[4]
    correct = text_split[5]
    add_question(text_question, ans1, ans2, ans3, ans4, correct)
    await message.answer("Вопрос добавлен, процесс завершен!")
    await state.clear()


@dp.message(Command('questions'))
async def add_questions(message: Message, state: FSMContext):
    delete_all_questions()
    await message.answer("Добавьте вопрос по шаблону\nTEXT;ans1;ans2;ans3;ans4;correct")
    await state.set_state(AddQuestion.a1)
            
            
@dp.message(Command('startgame'))
async def startgame(message: Message):
    user = get_user_by_id(message.from_user.id)
    if user[2]:
        change_game_status('ON')


@dp.message(Command('stopgame'))
async def startgame(message: Message):
    user = get_user_by_id(message.from_user.id)
    if user[2]:
        change_game_status('OFF')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())