import asyncio
import types

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from google_sheets import sheet_values_cat1
from keyboards.default.screens import screen1, screen2, screen_main_FAQ, screen_categories
from keyboards.inline.choice_buttons import start_menu_keyboard, main_menu_FAQ_keyboard
from loader import dp, bot


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(text='Добро пожаловать! \n Это чат-бот для команды маркетинга компании Eurotec!')
    await asyncio.sleep(2)
    await message.answer(text='Давай расскажу, чем я могу быть полезен 😉',
                         reply_markup=screen1)

@dp.message_handler(Text(equals='📦 Узнать информацию по товарным позициям'))
async def telling_info_item(message: Message):
    await message.answer(text='Выбери, категорию товара, чтобы получить актуальную информацию:', reply_markup=screen_categories)

@dp.message_handler(Text(equals='Товары Eurotec'))
async def telling_info_item(message: Message):
    await message.answer(sheet_values_cat1) # добавить клавиатурау return_to_menu

@dp.message_handler(Text(equals="Расскажи, чем полезен"))
async def telling_about_bot(message: Message):
    await message.answer(text='Отлично! \n'
                              'Здесь ты сможешь ускорить свою работу и не переключаться из мессенджера в другие '
                              'приложения, а общаться с клиентами и получать полезную информацию о работе в одном месте! '
                              '\n '
                              '\n'
                              'Я буду полезен, если тебе  нужно: \n'
                              '\n'
                              '- 📅 Создать и редактировать список задач на день  \n'
                              '- 📦 Получить актуальную информацию по товарам \n'
                              '- 📋 Создать КП для вашего клиентам на бланке  \n'
                              '- 🕐 Подсчитать количество времени, которое было потрачено на работу сегодня  \n'
                              '\n'
                              'Новые функции будут появляться 😉 ', reply_markup=screen2)


@dp.message_handler(Text(equals="К работе!"))
async def main_FAQ(message: Message):
    await message.answer(text='Выбери, что нужно  сделать тебе сейчас, я всегда помогу', reply_markup=screen_main_FAQ)

@dp.message_handler(Command('menu'))
async def main_FAQ(message: Message):
    await message.answer(text='Выбери, что нужно  сделать тебе сейчас, я всегда помогу', reply_markup=screen_main_FAQ)






