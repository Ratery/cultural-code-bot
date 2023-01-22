from aiogram import types, Dispatcher
from main import dp, bot
from keyboards import kb_client


async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=kb_client)


async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", )


"""@dp.callback_query_handler(func=lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')"""


async def empty(message: types.Message):
    await message.answer('Я не понимаю')


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_command_1, commands=['1'])
    dp.register_message_handler(empty)
