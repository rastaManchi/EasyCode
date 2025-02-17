from aiogram import types, Dispatcher, Bot
import aiogram.dispatcher.filters as filters
from aiogram.utils import executor
import random
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='7688359670:AAEf_gRt00OOD0Zil38X3LALoYE-F5ZupOA',parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
gameboard=types.ReplyKeyboardMarkup(one_time_keyboard=True)
gameboard.add("как выличить задницу")
gameboard.add("заказать воду")

class A7(StatesGroup):
    volume = State()
    gus = State()
    adress = State()

@dp.message_handler(commands="start")
async def welcome(message):
    await message.answer('сыграем в русскую рулетку..',reply_markup=gameboard)

@dp.message_handler(commands="roll")
async def roll(message):
    text=message.text
    number1=text.split(" ")[1]
    number2=text.split(" ")[2]
    dice=random.randint(int(number1),int(number2))
    await message.answer('крутится барабан')
    await message.answer(f'выпало:{dice}')

@dp.message_handler(commands="shoot")
async def shoot(message):
    await message.answer('выстрел')
    bullet = random.randint(1, 6)
    userluck = random.randint(1, 6)
    if bullet == userluck:
        await message.answer('вы здохли')
    else:
        await message.answer('вы выжили радуйтесь пока можете...')

async def nthn4trtghj4(message,state):
    if message.text == "заказать воду":
        await message.answer("точно воду a то вам все 30")
        await message.answer("сколько литров")

        await A7.volume.set()

async def volume(message,state):
    text = message.text
    await state.update_data(volume=message.text)
    await message.answer("газированая?")
    await A7.gus.set()
async def gus(message,state):
    gas = message.text
    await message.answer("кула доставить")
    await A7.adress.set()
async def adress(message,state):
    address = message.text
    await message.answer("кула доставить")
    await state.finish()
    
@dp.message_handler(filters.Text(equals="как выличить задницу",ignore_case=True))
async def gvghnchvg(message):
    await message.answer('<b>💩боярешне форте эвалар надёжный дуг вашей задницы усилиный каллий и магний он надолго сохранит здоровье вашей задницы, боярешне эвалар от компании СЕРЬёЗНОГО ПОНОСА💩 </b>')

def water(dp: Dispatcher):
    dp.register_message_handler(nthn4trtghj4)
    dp.register_message_handler(volume,state = A7.volume)
    dp.register_message_handler(gus,state = A7.gus)
    dp.register_message_handler(adress,state = A7.adress)
water(dp)

executor.start_polling(dp, skip_updates=True)