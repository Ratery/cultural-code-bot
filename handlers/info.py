import json
from contextlib import suppress
from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.exceptions import TelegramBadRequest

router = Router()
with open('resources/etiquette_info/themes.json') as f:
    themes = json.load(f)


@router.message(Command("info"))
@router.message(Text("🎩 Этикет по темам"))
async def cmd_info(message: types.Message) -> None:
    await message.answer(
        text=clean_msg(
            """
            🎩 <b>Этикет по темам</b>
            <i>Используйте кнопки ниже для навигации</i>
            """
        ),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text=value['title'], callback_data=key)]
                for key, value in themes.items()
            ]
        )
    )


@router.callback_query(Text(themes.keys()))
async def handle_callback(callback: types.CallbackQuery) -> None:
    theme = callback.data
    with open(f'resources/etiquette_info/{theme}.html') as f:
        with suppress(TelegramBadRequest):
            await callback.message.edit_text(
                text=f"<b>{themes[theme]['title']}</b>\n{f.read()}",
                reply_markup=callback.message.reply_markup
            )
    await callback.answer()
