import datetime
from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print(f"Bot started at {datetime.datetime.now()}")


async def on_shutdown(_):
    print(f"Bot finished at {datetime.datetime.now()}")


executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
