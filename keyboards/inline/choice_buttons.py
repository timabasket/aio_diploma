from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TASK_SPREADSHEET



task_manager = InlineKeyboardMarkup(row_width=2)

go_to_spreadsheet = InlineKeyboardButton(text="Таблица", url=TASK_SPREADSHEET, callback_data="spreadsheet")
task_manager.insert(go_to_spreadsheet)

task_is_done = InlineKeyboardButton(text="Заполнил таблицу", callback_data="Done")
task_manager.insert(task_is_done)

go_to_main_menu =  InlineKeyboardButton(text="Отмена", callback_data="go_back")
task_manager.add(go_to_main_menu)

timer_keyboard = InlineKeyboardMarkup(row_width=2)

start_timer = InlineKeyboardButton(text="Запустить таймер", callback_data="start_timer")
timer_keyboard.insert(start_timer)

stop_timer = InlineKeyboardButton(text="Посмотреть своё время", callback_data="stop_timer")
timer_keyboard.insert(stop_timer)

go_to_main_menu =  InlineKeyboardButton(text="Отмена", callback_data="go_back")
timer_keyboard.add(go_to_main_menu)
