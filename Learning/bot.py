import datetime
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


async def on_startup(_):
    print(f"Bot started at {datetime.datetime.now()}")


async def on_shutdown(_):
    print(f"Bot finished at {datetime.datetime.now()}")


"""=================================CLIENT  PART================================="""


def get_help():
    return "Not need help."


@dp.message_handler(commands=["help", "start"])
async def first_commands(message: types.Message):
    try:
        if message.text == "/start":
            await bot.send_message(message.from_user.id, "Здравствуйте! Это хранилище книг. Чтобы узнать больше "
                                                         "введите /help")
        else:
            await bot.send_message(message.from_user.id, get_help())
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


"""=================================ADMIN   PART================================="""

"""=================================GENERAL PART================================="""


@dp.message_handler()
async def echo_send(message: types.Message):
    # send answer
    # 1 variant
    await message.answer(message.text)
    # # 2 variant
    # await message.reply(message.text)
    # # 3 variant
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
