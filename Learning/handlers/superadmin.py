from aiogram import types, Dispatcher
from create_bot import bot, database


async def confirmation_reg(message: types.Message):
    try:
        data = message.text.split(" ")
        if len(data) != 2:
            await bot.send_message(message.from_user.id,
                                   "You write invalid data to confirmation registration user as Admin. Need count of "
                                   "args 1 "
                                   "and this arg must be eval user_id")
        else:
            user_id = int(data[1])
            user = database.get_user(user_id)
            print(user)
            if user is None:
                await bot.send_message(message.from_user.id,
                                       "Sorry this user not found on database. I'm sorry to my exception.")
            elif user.status != "User":
                await bot.send_message(message.from_user.id,
                                       f"Sorry this user have status as '{user.status}'. It is not 'User'. I'm sorry to my "
                                       f"exception.")
            else:
                database.set_user_status(user, "Admin")
                await bot.send_message(user.id,
                                       "You status stay as 'Admin'. Write '/help' to know about new functions.")
                await bot.send_message(message.from_user.id, "User status set as 'Admin'.")
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(confirmation_reg, commands=['confirmation'])
    print("Register by SuperAdmin-handlers")
