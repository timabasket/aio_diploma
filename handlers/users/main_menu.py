import asyncio
import textwrap
import types
import time
from io import BytesIO

import sys
import os
from os import listdir

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InputFile
from PIL import Image, ImageDraw, ImageFont
from aiogram.types import Message, CallbackQuery
from google_sheets import sheet_values_cat1, sheet_values_list
from keyboards.default.screens import screen1, screen2, screen_main_FAQ, screen_categories, screen_return_button, \
    screen_subcategories_return, timer_return_button
from keyboards.inline.choice_buttons import task_manager, timer_keyboard
from aiogram.dispatcher.filters.state import StatesGroup, State
from loader import dp, bot


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(text='Добро пожаловать! \n Это чат-бот для команды маркетинга компании Eurotec!')
    await asyncio.sleep(2)
    await message.answer(text='Давай расскажу, чем я могу быть полезен 😉',
                         reply_markup=screen1)


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


@dp.message_handler(Text(equals=['📦 Узнать информацию по товарным позициям', 'Информация по другим категориям']))
async def telling_info_item(message: Message):
    await message.answer(text='Выбери, категорию товара, чтобы получить актуальную информацию:',
                         reply_markup=screen_categories)

# обработчик вывода информации по категориям товаров из гугл таблицы
@dp.message_handler(Text(equals='Товары Eurotec'))
async def telling_info_item(message: Message):
    await message.answer(sheet_values_cat1, reply_markup=screen_subcategories_return)  # добавить клавиатуру return_to_menu


@dp.message_handler(Text(equals='Топ-10 товаров'))
async def telling_info_item(message: Message):
    await message.answer(text='здесь будет список другой категории',
                         reply_markup=screen_subcategories_return)  # добавить клавиатуру return_to_menu

# обработчик фукнции НАЗАД
@dp.message_handler(Text(equals='В меню'))
async def returning_back(message: Message):
    await message.answer(text='В меню', reply_markup=screen_main_FAQ)

# обработчик показывающий расписание
@dp.message_handler(Text(equals='📅 Создать список задач'))
async def telling_tasks(message: Message):
    await message.answer(text='Чтобы создать список задач перейдите в таблицу и заполните её',
                         reply_markup=task_manager)

#таблица заполнена
@dp.callback_query_handler(text_contains="Done")
async def telling_cur_tasks(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(sheet_values_list, reply_markup=screen_return_button)

@dp.callback_query_handler(text="go_back")
async def telling_cur_tasks(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(text='В меню', reply_markup=screen_main_FAQ)

# обработчик рабочего секундомера
@dp.message_handler(Command('timer'))
async def timer(message: Message):
    await message.reply(text='Чтобы запустить таймер рабочего времени нажмите на кнопку ', reply_markup=timer_keyboard)
    #await message.answer(cache_time=60)
    #await message.reply(text=f'Ваш id {user_id}'.format(user_id))

# Запуск таймер пользователем
@dp.callback_query_handler(text="start_timer")
async def start_timer(call: CallbackQuery):
    user_id = str(call.chat.id)
    timer_data_dict = {}
    _user_time = time.time()
    timer_data_dict[user_id()] = start_timer()
    await call.answer(text='Ваш словарь{}', reply_markup=screen_return_button)
    await call.answer(text='Таймер запушен', reply_markup=screen_return_button)


# Остановка таймер пользователем
@dp.callback_query_handler(text="stop_timer")
async def stop_timer(call: CallbackQuery):
    delta = time.time() - start_timer
    hours = int((delta // 60) // 60)
    minutes = int((delta // 60) - (hours * 60))
    seconds = round(delta - minutes * 60 - hours * 60 * 60)
    final_time = f"Ваше время: {'{:02}'.format(hours)}:{'{:02}'.format(minutes)}:{'{:02}'.format(seconds)}"

    stop_timer(start_timer.timer_data_dict.get(get_user_id()))
    await call.answer(final_time, reply_markup=timer_return_button)

class UserState(StatesGroup):
    pick_text = State()

# Обработчик вывода КП с текстом пользователя
@dp.message_handler(Text(equals='📋 Создать КП'))
async def sending_a_photo(message: Message):
    await message.answer(text='Введите ваши товарные позиции сообщением:')
    await UserState.pick_text.set()
#состояние принятия текста от пользователя
@dp.message_handler(state=UserState.pick_text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text_for_pick=message.text)
    await message.answer("Отлично! КП принято")
    data = await state.get_data()
    data_text = data.get('text_for_pick')

    # Перенос текста
    wrapper = textwrap.TextWrapper(width=50)
    word_list = wrapper.wrap(text=data_text)
    text_new = ''
    for ii in word_list[:-1]:
        caption_new = text_new + ii + '\n'
    text_new += word_list[-1]

    # создание коммерческого предложения с уникальным текстом
    im = Image.open("D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Диплом\\aio_diploma\data\КП.jpg")
    # получаем В и Ш
    im_width, im_height = im.size
    # fix start text position
    text_width = 140
    text_height = 1020
    # get max width of text area
    max_width = im_width - text_width
    max_height = im_height - text_height - 400 # 400 пикселей нижний колонтитул
    font = ImageFont.truetype('D:\ОСНОВНОЕ\шрифты\HelveticaRegular.ttf', size=65)
    font_height = font.getsize(data_text)[1]
    # отформатированный текст
    new_text = ''
    # если длина текста превысила размер текстового поля
    if font.getsize(data_text)[0] >= max_width:
        lined_text = data_text.split('\n')
        # проверяем строки в тексте на вместимость
        for line in lined_text:
            # если длина строки превышает размер текстового поля
            if font.getsize(line)[0] >= max_width:
                # разбиваем строку на слова
                temp_text = line.split()
                temp_line = ''
                temp_line2 = ''
                # номер рассматриваемого слова
                i = 0
                # идём по всем словам строки и пытаемся вместить
                while i < len(temp_text):
                    # проверка НЕ превышает ли слово размер текстового поля
                    if font.getsize(temp_text[i])[0] >= max_width:
                        print('Error')
                        temp_line = 'Error line'
                        break
                    # добавляем слова пока вмешаются в строку текстового поля
                    while i < len(temp_text) and font.getsize(temp_line2 + temp_text[i])[0] < max_width:
                        temp_line2 += temp_text[i] + ' '
                        i += 1
                    else:
                        # Если мы достигли лимит строки, то создаём новую строку, а старую сохр.
                        if i < len(temp_text):
                            temp_line += temp_line2 + '\n'
                        else:
                            temp_line += temp_line2
                        temp_line2 = ''
                # сохранение отформатированной строки
                new_text += temp_line + '\n'
            else:
                new_text += line + '\n'
    else:
        new_text = data_text
    data_text = new_text
    # проверка пользователя на дурака + подсказка
    if new_text.count('\n') * font_height > max_height:
        data_text = f"Достигнут лимит строк\n Разбейте текст на два сообщения, \nМаксимальное количесвто строк на листе: {int(max_height / font_height)}"

    # Создаем объект со шрифтом
    draw_text = ImageDraw.Draw(im)
    draw_text.multiline_text(
        (text_width, text_height),
        text=data_text,  #должен получать текст от пользователя и передовать его в модуль
        # Добавляем шрифт к изображению
        font=font,
        spacing=15,
        fill='#1C0606')
    #Сохраняем картинку в нужном разрешении и с нужным названием
    im.save('D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Диплом\\aio_diploma\data\photo\image.PNG')
    photo = open('D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Диплом\\aio_diploma\data\photo\image.PNG', 'rb')
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo
    )
    directory = "D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Диплом\\aio_diploma\data\photo"
    test = os.listdir(directory)

    for item in test:
        if item.endswith(".PNG"):
            os.remove(os.path.join(directory, item))
    await state.finish()

# Обработчик общей информации о боте
@dp.message_handler(Text(equals='❓ Справка'))
async def telling_info(message: Message):
    await message.answer(text=
    'Есть вопросы?\n'
    'Чтобы перезапустить чат-бот отправь сообщение:\n' 
    'start\n'
    'Разработчик чат-бота:\n'
    'Изместьев Тимофей - студент 4 курса ФСПОиДП НИУ РАНХиГС'
    ,reply_markup=screen_return_button)


# обработчик для возврата в главное меню черзе команду
@dp.message_handler(Command('menu'))
async def main_FAQ(message: Message):
    await message.answer(text='Выбери, что нужно  сделать тебе сейчас, я всегда помогу', reply_markup=screen_main_FAQ)
