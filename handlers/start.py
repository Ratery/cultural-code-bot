from aiogram import Router, types
from aiogram.filters.command import CommandStart

from keyboards import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: types.Message) -> None:

    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=main_menu_keyboard)
