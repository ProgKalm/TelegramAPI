import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    # send answer
    # 1 variant
    await message.answer(message.text)
    # # 2 variant
    # await message.reply(message.text)
    # # 3 variant
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)