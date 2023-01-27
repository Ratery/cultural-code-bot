from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command("help"))
async def cmd_help(message: types.Message) -> None:
    await message.reply(clean_msg(
        """
        🎩 <b>Данный бот создан в рамках проекта <a href="https://t.me/cultural_code_lyceum">Культурный код</a></b>
        Он предназначен для повышения уровня знания культуры и правил этикета в интересном и развлекательном формате.\n
        🛠 <b>Разработчики</b>
        <b>1. <a href="https://t.me/TheRatery">Ratery</a></b>
        <b>2. <a href="https://t.me/urMister">EL$E</a></b>
        """
    ))
