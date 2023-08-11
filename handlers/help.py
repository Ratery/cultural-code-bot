from inspect import cleandoc as clean_msg

from aiogram import F
from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command("help"))
@router.message(F.text == "❔ Помощь")
async def cmd_help(message: types.Message) -> None:
    await message.answer(clean_msg(
        """
        🎩 <b>Данный бот создан в рамках проекта <a href="https://t.me/cultural_code_lyceum">Культурный код</a></b>
        Он предназначен для повышения уровня знания культуры и правил этикета в интересном и развлекательном формате.
        
        ❔ <b>Команды</b>
        <i>Используйте кнопки под клавиатурой и/или приведённые команды для навигации</i>
        /start — Перезапустить бота
        /quiz — Пройти тест по знаниям этикета
        /info — Краткая информация по темам этикета
        /authors — Информация о разработчиках
        /help — Помощь
        
        🛠 <b>Разработчики</b>
        <b>• <a href="https://t.me/TheRatery">Ratery</a></b>
        <b>• <a href="https://t.me/urMister">EL$E</a></b>
        
        💻 <b>Исходный код</b>
        Исходный код бота доступен на <a href="https://github.com/Ratery/cultural-code-bot">GitHub</a>.
        """
    ))
