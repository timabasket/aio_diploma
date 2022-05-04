from aiogram import types
from loader import dp, bot


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
    await message.reply('Ты написал мне это ⬆️\n Но лучше воспользуйся меню /menu')