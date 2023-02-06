from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command("developers", "authors"))
async def cmd_developers(message: types.Message) -> None:
    await message.answer(
        text=clean_msg(
            f"""
            🛠 <b>Разработчики</b>
            <i>Люди, непосредственно принимавшие участие в разработке бота</i>
            <b>• <a href="https://t.me/TheRatery">Ratery</a></b>
            <b>• <a href="https://t.me/urMister">EL$E</a></b>
            
            <b>👤 Благодарности</b>
            <i>Выражаем благодарность остальным членам нашей команды за подачу идей и поддержку</i>
            <b>• @scorpiann1</b>
            <b>• @tidashka</b>
            <b>• @curly1iana</b>
            
            <b>🎓 Ученикам 9 класса лицея</b>
            Если Вы являетесь учеником 9 класса лицея им. Н. И. Лобачевского и заинтересованы в дальнейшем развитии проекта в рамках индивидульной проектной деятельности на протяжении 10 класса, свяжитесь с <a href="https://t.me/TheRatery">Ratery</a>.
            В начале учебного года мы предоставим Вам исходный код бота и делегируем управление каналом.
            
            <b>💻 Исходный код</b>
            Исходный код бота доступен на <a href="https://github.com/Ratery/cultural-code-bot">GitHub</a>.
            """
        ),
        disable_web_page_preview=True
    )
