from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_1 = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(btn_1)
