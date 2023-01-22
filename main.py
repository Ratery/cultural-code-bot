import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config import TOKEN

logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
