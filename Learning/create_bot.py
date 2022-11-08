import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

database = None
user_help: dict = None
