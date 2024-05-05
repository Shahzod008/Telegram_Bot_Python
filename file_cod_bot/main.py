from aiogram import types, filters, Dispatcher
from pathlib import Path
import keyboard
import logging
import asyncio
import config
import callb

dp = Dispatcher()
BASE_DIR = Path(__file__).resolve().parent.parent


@dp.message(filters.CommandStart())
async def start(message: types.Message):
    file_photo = f"../source/Приветствие/Приветствие.png"
    file = types.FSInputFile(path=file_photo)
    await message.answer_photo(file)
    await message.answer(text=f"Привет <b>{message.from_user.first_name}</b>. Выбери что тебя интересует",
                         reply_markup=keyboard.kb_start.as_markup())


@dp.callback_query()
async def hand(callback: types.CallbackQuery):
    await callb.handlers(callback)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(config.bot)

if __name__ == "__main__":
    asyncio.run(main())
