from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard(slides_dict: dict):
    keyboard_data = [
        [KeyboardButton(text="КУПИТЬ БИЛЕТ")]
    ]
    for slide_name in slides_dict:
        keyboard_data.append([KeyboardButton(text=slide_name)])
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_data, resize_keyboard=True)
    return keyboard