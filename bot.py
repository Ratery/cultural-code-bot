from aiogram.utils import executor
from main import dp

from handlers import client, admin, other

client.register_client_handlers(dp)
admin.register_admin_handlers(dp)
other.register_other_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
