from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token = '6943333150:AAGA-uXOML1M88KaLtslNoXzF46eJZm7yxU', parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
admin = 190203478


class Buy(StatesGroup):
    name = State()
    age = State()
    phone = State()


slides_dict = {}
file = open('slides.txt', 'r', encoding='utf-8')
slides = file.read().split('\n')
for slide in slides:
    slide_info = slide.split(':')
    slides_dict[slide_info[0]] = slide_info[1:]
    
async def start(message: types.Message):
    print(message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('КУПИТЬ БИЛЕТ')
    for slide in slides_dict:
        keyboard.add(slide)
    await message.answer('Привет', reply_markup=keyboard)
    
async def keyboard_event(message: types.Message):
    if message.text == 'КУПИТЬ БИЛЕТ':
        await message.answer('Сколько вам лет?')
        await Buy.age.set()
    else:
        name = message.text
        slide_info = slides_dict[name]
        await message.answer(slide_info)
        
async def name_waiting(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('введите ваш номер телефона: ')
    await Buy.phone.set()
    
async def age_waiting(message: types.Message, state: FSMContext):
    age = int(message.text)
    if age >= 18:
        await state.update_data(age=message.text)
        await message.answer('Как вас зовут? ')
        await Buy.name.set()
    else:
        await message.answer('Ты еще слишком мал...')
        await state.finish()
    
async def phone_waiting(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone=message.text)
        await message.answer('Поздравляем, вы купили билет!')
        data = await state.get_data()
        message_text = f'Имя: {data["name"]}\nВозраст: {data["age"]}\nТелефон: {data["phone"]}'
        await bot.send_message(admin, message_text)
        await state.finish()
    else:
        await message.answer('введите ваш номер телефона: ')
    
    
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(keyboard_event)
    dp.register_message_handler(name_waiting, state=Buy.name)
    dp.register_message_handler(age_waiting, state=Buy.age)
    dp.register_message_handler(phone_waiting, state=Buy.phone)
    
register_handlers(dp)

executor.start_polling(dp, skip_updates=True)