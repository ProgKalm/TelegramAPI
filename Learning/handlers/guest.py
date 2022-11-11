from aiogram import types, Dispatcher
from create_bot import database, User, bot, get_user_status, get_user_by_msg


async def registrate_simple_user(message: types.Message):
    try:
        user = get_user_by_msg(message)
        user.status = get_user_status(user.id) if get_user_status(user.id) is not None else "Guest"
        do = "was"
        if user.status == "Guest":
            do = "will"
            database.set_user_status(user, "User")
        msg = f"You {do} registrate on this bot. Write '/help' to see new function for you."
        await bot.send_message(message.from_user.id, msg)
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


async def out(message: types.Message):
    try:
        user = get_user_by_msg(message)
        user.status = "Guest"
        database.set_user_status(user, "Guest")
        msg = f"You status set as Guest. To re-registrate write '/registrate'"
        await bot.send_message(message.from_user.id, msg)
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registrate_simple_user, commands=['registrate'])
    dp.register_message_handler(out, commands=['out'])
    print("Register by Guests-handlers")
