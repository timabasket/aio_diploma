from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

screen1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расскажи, чем полезен"),
            KeyboardButton(text="К работе!")
        ],
    ],
    resize_keyboard=True
)

screen2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="К работе!")
        ],
    ],
    resize_keyboard=True
)
screen_main_FAQ_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📅 Создать список задач'),
            KeyboardButton('📋 Создать КП')

        ],
        [
            KeyboardButton('📦 Узнать информацию по товарным позициям')
        ],
        [
            KeyboardButton('🕐 Подсчитать количество рабочего времени')
        ],
        [
            KeyboardButton('❓ Справка')
        ]
    ]
)

# кнопка возврата
return_button = KeyboardButton('В меню')


# тут кнопки для основного меню
work_list_button = KeyboardButton ('📅 Создать список задач')
make_propose_button = KeyboardButton ('📋 Создать КП')
know_item_info_button = KeyboardButton('📦 Узнать информацию по товарным позициям')
count_work_time_button = KeyboardButton ('🕐 Подсчитать количество рабочего времени')
info_about_bot_button = KeyboardButton('❓ Справка')

screen_main_FAQ = ReplyKeyboardMarkup(resize_keyboard=True)
screen_main_FAQ.row(work_list_button, make_propose_button).add(know_item_info_button).add(count_work_time_button).add(info_about_bot_button)

# тут кнопки для блока информации по категориям
cat1_button =  KeyboardButton ('Товары Eurotec')
cat2_button =  KeyboardButton ('Топ-10 товаров')
categories_return = KeyboardButton('Информация по другим категориям')
screen_categories = ReplyKeyboardMarkup(resize_keyboard=True)
screen_categories.row(cat1_button, cat2_button).add(return_button)

# подкатегории раздела "Информация по товарам"
screen_subcategories_return = ReplyKeyboardMarkup(resize_keyboard=True)
screen_subcategories_return.row(return_button, categories_return)

#постоянная кнопка
screen_return_button = ReplyKeyboardMarkup(resize_keyboard=True)
screen_return_button.add(return_button)

#возврат в меню таймера
timer_return_button = ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
timer_menu_return_button = KeyboardButton('Запустить новый таймер') #кнопка
timer_return_button.row(timer_menu_return_button, return_button)

