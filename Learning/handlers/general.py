import json
import sys

from aiogram import types, Dispatcher
from create_bot import bot, database, user_help, get_user_status, get_user_by_msg


async def start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               "Hello, lets started! To start: try to know how can you work with me by run command "
                               "'/help'")
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    user = get_user_by_msg(message)
    database.add_user(user)
    await message.delete()


async def get_user_type(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, get_user_status(message.from_user.id))
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


def get_help(message: types.Message):
    global user_help
    try:
        if user_help is None:
            with open(fr"{sys.path[0]}\\handlers\\users_help.json", "r", encoding="utf-8") as file:
                user_help = json.loads(file.read())

        result = ""
        user_type = get_user_status(message.from_user.id)
        if user_type is None:
            user = get_user_by_msg(message)
            database.add_user(user)
            user_type = user.status
        while user_type is not None:
            data: dict = user_help[user_type]
            user_type = data.get("href")
            for key in data:
                if key != "href":
                    result = result + f"{key} - {data[key]}\n"

        return result.strip()
    except Exception as ex:
        return f"/report - Please report about exception(also push its command)"


async def help_data(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, get_help(message))
    except Exception as ignored:
        await message.answer("Общение с ботом через ЛС, напишите ему: @book_getter_bot")
    await message.delete()


async def report(message: types.Message):
    await message.delete()


async def echo_send(message: types.Message):
    await message.reply(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(help_data, commands=['help'])
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(report, commands=['report'])
    dp.register_message_handler(get_user_type, commands=['usertype'])
    dp.register_message_handler(echo_send)
    print("Register by General-handlers")
