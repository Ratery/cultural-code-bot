from aiogram import Router, types
from aiogram.filters.command import CommandStart

router = Router()

@router.message(CommandStart())
async def process_start_command(message: types.Message) -> None:
    await message.reply("Привет!\nНапиши мне что-нибудь!")
