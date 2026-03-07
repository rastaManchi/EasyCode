from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def contact_keyboard():
    keyboard_ = [
        [KeyboardButton(text="Поделиться контактом", request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_, resize_keyboard=True)
    return keyboard
