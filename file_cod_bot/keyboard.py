from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dannie import buttons_1, buttons_2, buttons_3, buttons_4
from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_buttons_from_dict(inline_kb, data):
    for button_text, callback_data in data.items():
        inline_kb.button(text=button_text, callback_data=callback_data)
    inline_kb.adjust(1)


kb_start = InlineKeyboardBuilder()
kb_ras = InlineKeyboardBuilder()
kb = InlineKeyboardBuilder()
kb_teorija_uroka = InlineKeyboardBuilder()

add_buttons_from_dict(kb_start, buttons_1)
add_buttons_from_dict(kb_ras, buttons_2)
add_buttons_from_dict(kb, buttons_3)
add_buttons_from_dict(kb_teorija_uroka, buttons_4)

kb_back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="В главное меню", callback_data="back")]])
