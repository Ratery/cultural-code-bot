import os
import asyncio
import logging
import importlib

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from middlewares.throttling import ThrottlingMiddleware


def load_handlers(dp: Dispatcher) -> None:
    handlers = [m[:-3] for m in os.listdir('./handlers') if m.endswith('.py')]
    for handler in handlers:
        try:
            module = importlib.import_module(f'handlers.{handler}')
            dp.include_router(getattr(module, 'router'))
        except AttributeError:
            raise AttributeError(f"Module '{handler}' has no attribute 'router'")


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode='HTML')

    dp = Dispatcher(storage=MemoryStorage())
    dp.message.filter(F.chat.type == 'private')
    dp.message.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(ThrottlingMiddleware())

    logging.log(
        level=logging.INFO,
        msg=f"Bot running as @{(await bot.get_me()).username}"
    )
    load_handlers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
