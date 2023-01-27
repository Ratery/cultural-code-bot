from aiogram import types

main_menu_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="🎩 Этикет по темам"),
            types.KeyboardButton(text="📙 Пройти тест"),
            types.KeyboardButton(text="❔ Помощь")
        ],
    ],
    resize_keyboard=True
)