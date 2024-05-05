from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

buttons_1 = {
    "Расписание": "raspisanie",
    "Главное меню": "back",
    "Тех. поддержка": "tech_support",
}

buttons_2 = {
    "Понедельник": "panidelnik",
    "Вторник": "vtornik",
    "Среда": "sreda",
    "Четверг": "chetverg",
    "Пятница": "pjatniza",
    "В главное меню": "back",
}

buttons_3 = {
    "Расписание": "raspisanie",
    "Доп. уроки": "dop_uroki",
    "Теория уроков": "lesson_theory",
    "Преподователи": "prepodovateli",
    "Список учеников": "spisok_uchenikov",
    "Задачи": "inter_zadachi",
    "Календарь учебного года": "kalendar",
}

buttons_4 = {
    "Албебра": "albebra",
    "Русиш": "rusish",
    "Геометриш": "geomerish",
    "Шизика": "fisish",
    "В главное меню": "back",
}


kb_back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="В главное меню", callback_data="back")]])


def add_buttons_from_dict(inline_kb, data):
    for button_text, callback_data in data.items():
        inline_kb.button(text=button_text, callback_data=callback_data)


kb_start = InlineKeyboardBuilder()
kb_ras = InlineKeyboardBuilder()
kb = InlineKeyboardBuilder()
kb_teorija_uroka = InlineKeyboardBuilder()


add_buttons_from_dict(kb_start, buttons_1)
add_buttons_from_dict(kb_ras, buttons_2)
add_buttons_from_dict(kb, buttons_3)
add_buttons_from_dict(kb_teorija_uroka, buttons_4)
