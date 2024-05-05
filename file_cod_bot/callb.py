import os
from pathlib import Path

from keyboard import *
from dannie import *
from aiogram.types import CallbackQuery, InputFile, FSInputFile


# async def call(callback: CallbackQuery):
#     if callback.data == "tech_support":
#         await callback.message.answer_contact(phone_number="+79966636043", first_name=" ")
#         await callback.message.edit_text("Можете обращаться сюда", reply_markup=kb_back)
#     elif callback.data == "albebra":
#         await callback.message.answer_media_group(media=album_albebra.build())
#         await callback.message.edit_text(text=text1, reply_markup=kb_back)
#     elif callback.data == "rusish":
#         await callback.message.answer_media_group(media=album_rusish.build())
#         await callback.message.edit_text(text=text1, reply_markup=kb_back)
#     elif callback.data == "geomerish":
#         await callback.message.answer_media_group(media=album_geomerish.build())
#         await callback.message.edit_text(text=text1, reply_markup=kb_back)
#     elif callback.data == "fisish":
#         await callback.message.answer_media_group(media=album_fisish.build())
#         await callback.message.edit_text(text=text1, reply_markup=kb_back)
#     elif callback.data == "kalendar":
#         await callback.message.answer_photo(photo=FSInputFile(path='file/Календарь.jpg'))
#         await callback.message.edit_text("Не жди каникул", reply_markup=kb_back)


async def handlers(callback: CallbackQuery):
    request_data = callback.data
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
        "lesson_theory": lambda: send_menu(callback, "Выбери предмет", kb_teorija_uroka),
        "back": lambda: send_menu(callback, "че тебе", kb),
        "raspisanie": lambda: send_menu(callback, "Выберите день недели", kb_ras),
        "rusish": lambda: send_images(callback, "russish"),
        "geomerish": lambda: send_images(callback, "geometrish"),
        "fisish": lambda: send_images(callback, "fisish"),
        "albebra": lambda: send_images(callback, "albebra"),
        "kalendar": lambda: send_images(callback, "fk/kalendar"),
    }

    if request_data in data_to_message:
        await data_to_message[request_data]()


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
