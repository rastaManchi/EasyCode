from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    keyboard_data = [
        [KeyboardButton(text="Профиль"), KeyboardButton(text="Звук")],
        [KeyboardButton(text="Голосовое")],
        [KeyboardButton(text="Группа фото"), KeyboardButton(text="test")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_data, resize_keyboard=True)
    return keyboard
