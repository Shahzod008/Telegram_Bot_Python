from dannie import panidelnik, vtornik, sreda, chetverg, pjatniza
from keyboard import kb_teorija_uroka, kb, kb_ras, kb_back
from aiogram.types import CallbackQuery, FSInputFile
from pathlib import Path
import os


async def handlers(callback: CallbackQuery):
    data_to_message = {
        "ponidelnik": lambda: send_message(callback, panidelnik),
        "vtornik": lambda: send_message(callback, vtornik),
        "sreda": lambda: send_message(callback, sreda),
        "chetverg": lambda: send_message(callback, chetverg),
        "pjatniza": lambda: send_message(callback, pjatniza),
        "dop_uroki": lambda: send_message(callback, "Ну тут крч расписание доп. уроков"),
        "spisok_uchenikov": lambda: send_message(callback, "Список учащихся класса"),
        "prepodovateli": lambda: send_message(callback, "Список Учителей"),
        "inter_zadachi": lambda: send_message(callback, "Ты слишком тупой задачек для тебя нету"),
        "lesson_theory": lambda: send_menu(callback, "Выбери предмет", kb_teorija_uroka.as_markup()),
        "back": lambda: send_menu(callback, "че тебе", kb.as_markup()),
        "raspisanie": lambda: send_menu(callback, "Выберите день недели", kb_ras.as_markup()),
        "rusish": lambda: send_images(callback, "russish"),
        "geomerish": lambda: send_images(callback, "geometrish"),
        "fisish": lambda: send_images(callback, "fisish"),
        "albebra": lambda: send_images(callback, "albebra"),
        "kalendar": lambda: send_images(callback, "fk/kalendar"),
    }
    if callback.data in data_to_message:
        await data_to_message[callback.data]()


async def send_menu(callback, text, markup):
    await callback.message.edit_text(text, reply_markup=markup)


async def send_message(callback, message):
    await callback.message.edit_text(message, reply_markup=kb_back)

BASE_DIR = Path(__file__).resolve().parent.parent


async def send_images(callback, folder):
    adr = os.path.join(f"{BASE_DIR}/source/{folder}")
    for file_name in os.listdir(adr):
        file_open = FSInputFile(f"{BASE_DIR}/source/{folder}/{file_name}")
        await callback.message.answer_photo(file_open)

    await callback.message.answer("А все!", reply_markup=kb_back)
