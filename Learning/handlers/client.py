from aiogram import types
from create_bot import dp, bot

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
