from aiogram import types, Dispatcher
from create_bot import bot, database, get_user_status, get_user_by_msg


async def reg(message: types.Message):
    try:
        user = get_user_by_msg(message)
        user.status = get_user_status(user.id) if get_user_status(user.id) is not None else "Guest"
        if user.status == "User":
            await bot.send_message(message.from_user.id,
                                   "I send message about your to SuperAdmin, when he confirmation this I say it")
            super_admin = database.get_super_admin()
            await bot.send_message(super_admin.id,
                                   f"This user want to stay Admin. {user.__str__()}")
        elif user.status == "Guest":
            await bot.send_message(message.from_user.id,
                                   "You don't have permissions for this function. Write '/registrate'. And try again.")
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


async def author(message: types.Message):
    try:
        data = message.text.split(" ")
        if len(data) == 2:
            pass
        else:
            await bot.send_message(message.from_user.id,
                                   f"Sorry but your try is not valid this "
                                   f"function need also 1 parameter by author name.")
    except Exception as ignored:
        print(ignored.__class__)
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reg, commands=['reg'])
    dp.register_message_handler(author, commands=['author'])
    print("Register by User-handlers")
