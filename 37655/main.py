from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token = '6943333150:AAGA-uXOML1M88KaLtslNoXzF46eJZm7yxU', parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

slides_dict = {}
file = open('slides.txt', 'r', encoding='utf-8')
slides = file.read().split('\n')
for slide in slides:
    slide_info = slide.split(':')
    slides_dict[slide_info[0]] = slide_info[1:]
    
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    for slide in slides_dict:
        keyboard.add(slide)
    await message.answer('Привет', reply_markup=keyboard)
    
async def keyboard_event(message: types.Message):
    if message.text == 'КУПИТЬ БИЛЕТ':
        pass
    else:
        name = message.text
        slide_info = slides_dict[name]
        await message.answer(slide_info)
    
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(keyboard_event)
    
register_handlers(dp)

executor.start_polling(dp, skip_updates=True)