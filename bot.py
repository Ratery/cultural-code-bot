import os
import asyncio
import logging
import importlib

from aiogram import Bot, Dispatcher

from config import TOKEN

logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=TOKEN)
dp = Dispatcher()


def load_handlers() -> None:
    handlers = [m[:-3] for m in os.listdir("./handlers") if m.endswith(".py")]
    for handler in handlers:
        try:
            module = importlib.import_module(f"handlers.{handler}")
            dp.include_router(getattr(module, 'router'))
        except AttributeError:
            raise AttributeError(f"Module '{handler}' has no attribute 'router'")


async def main() -> None:
    logging.log(
        level=logging.INFO,
        msg=f"Bot running as @{(await bot.get_me()).username}"
    )
    load_handlers()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
