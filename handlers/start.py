from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import CommandStart

from keyboards import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: types.Message) -> None:
    await message.answer(
        text=clean_msg(
            f"""
            👋 Привет, <b>{message.from_user.full_name}</b>!
            Используй кнопки под клавиатурой для навигации.
            """
        ),
        reply_markup=main_menu_keyboard
    )
