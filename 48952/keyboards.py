from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard():
    keyboard_data = [
        [KeyboardButton(text="Профиль"), KeyboardButton(text="test")],
        [KeyboardButton(text="test")],
        [KeyboardButton(text="test"), KeyboardButton(text="test")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_data, resize_keyboard=True)
    return keyboard


def inline_keyboard():
    keyboard_data = [
        [InlineKeyboardButton(text='Test', callback_data='test_btn')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_data)
    return keyboard