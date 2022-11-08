from aiogram import types


@dp.message_handler()
async def echo_send(message: types.Message):
    # send answer
    # 1 variant
    await message.answer(message.text)
    # # 2 variant
    # await message.reply(message.text)
    # # 3 variant
    # await bot.send_message(message.from_user.id, message.text)
