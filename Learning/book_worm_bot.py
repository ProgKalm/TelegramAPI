import datetime
from aiogram.utils import executor
from create_bot import dp, database
from handlers import *


async def on_startup(_):
    print(f"Bot started at {datetime.datetime.now()}")


async def on_shutdown(_):
    database.close()
    with open("d.txt", "w") as file:
        file.write("File closed")
    print(f"Bot finished at {datetime.datetime.now()}")


superadmin.register_handlers(dp)
admin.register_handlers(dp)
user.register_handlers(dp)
guest.register_handlers(dp)
general.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
