import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def main_keyboard():
    keyboard_buttons = [
        [KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Пока")],
        [KeyboardButton(text="1"), KeyboardButton(text="2")]
    ]
    
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_buttons)
    return keyboard


async def test_inline():
    keyboard_buttons = [
        [InlineKeyboardButton(text="test", callback_data="test_btn")]
    ]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    return keyboard