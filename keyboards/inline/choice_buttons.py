from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import start_menu_callback


start_menu_keyboard = InlineKeyboardMarkup(row_width=2)

tell_me_about = InlineKeyboardButton(text='Расскажи, чем полезен', callback_data=start_menu_callback.new(
                item_name="tell_me_about"
            ))
start_menu_keyboard.insert(tell_me_about)

main_FAQ = InlineKeyboardButton(text="К работе!", callback_data=start_menu_callback.new(
                item_name="main_FAQ"
))
start_menu_keyboard.insert(main_FAQ)

# пока не использую
main_menu_FAQ_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='К работе!')
        ]
    ]
)

