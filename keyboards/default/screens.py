from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

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
screen_categories = ReplyKeyboardMarkup(resize_keyboard=True)
screen_main_FAQ.row(cat1_button, cat2_button)


