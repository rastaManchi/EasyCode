from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token = '6943333150:AAGA-uXOML1M88KaLtslNoXzF46eJZm7yxU', parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

file = open('slides.txt', 'r', encoding='utf-8')
slides = file.read().split('\n')
print(slides)


executor.start_polling(dp, skip_updates=True)