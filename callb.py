from keyboard import *
from dannie import *
from media import *
from aiogram.types import FSInputFile, CallbackQuery


async def call(callback: CallbackQuery):
    data = {
        "ponidelnik": panidelnik,
        "vtornik": vtornik,
        "sreda": sreda,
        "chetverg": chetverg,
        "pjatniza": pjatniza,
    }

    if callback.data in data:
        message = data[callback.data]
        await callback.message.edit_text(message, reply_markup=kb_back)

    data_to_range = {
        "albebra": text1,
        "rusish": text1,
        "geomerish": text1,
        "fisish": text1,
    }

    if callback.data in data_to_range:
        args = data_to_range[callback.data]
        foto(*args, user_id=user_id)

    if callback.data == "raspisanie":
        await callback.message.edit_text("Выберите день недели", reply_markup=kb_ras)
    elif callback.data == "tech_support":
        await callback.message.answer_contact(phone_number="+79966636043", first_name=" ")
        await callback.message.edit_text("Можете обращаться сюда", reply_markup=kb_back)
    elif callback.data == "dop_uroki":
        await callback.message.answer_photo(photo=FSInputFile(path='file/уроки.png'))
        await callback.message.edit_text("Не опаздывай на доп. уроки", reply_markup=kb_back)
    elif callback.data == "lesson_theory":
        await callback.message.edit_text("Выбери предмет", reply_markup=kb_teorija_uroka)
    elif callback.data == "albebra":
        await callback.message.answer_media_group(media=album_albebra.build())
        await callback.message.edit_text(text=text1, reply_markup=kb_back)
    elif callback.data == "rusish":
        await callback.message.answer_media_group(media=album_rusish.build())
        await callback.message.edit_text(text=text1, reply_markup=kb_back)
    elif callback.data == "geomerish":
        await callback.message.answer_media_group(media=album_geomerish.build())
        await callback.message.edit_text(text=text1, reply_markup=kb_back)
    elif callback.data == "fisish":
        await callback.message.answer_media_group(media=album_fisish.build())
        await callback.message.edit_text(text=text1, reply_markup=kb_back)
    elif callback.data == "Istorija_klassa":
        await callback.message.edit_text("Фоточки и видосики класса", reply_markup=kb_back)
    elif callback.data == "spisok_uchenikov":
        await callback.message.edit_text("Список учащихся класса", reply_markup=kb_back)
    elif callback.data == "prepodovateli":
        await callback.message.edit_text("Список Учителей", reply_markup=kb_back)
    elif callback.data == "inter_zadachi":
        await callback.message.edit_text("Ты слишком тупой задачек для тебя нету", reply_markup=kb_back)
    elif callback.data == "kalendar":
        await callback.message.answer_photo(photo=FSInputFile(path='file/Календарь.jpg'))
        await callback.message.edit_text("Не жди каникул", reply_markup=kb_back)
    elif callback.data == "back":
        await callback.message.edit_text("Главное меню", reply_markup=kb)
