import asyncio
import logging
import config
from callb import call
from keyboard import *
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

bot = Bot(token=config.Bot_token, parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    if message.from_user.id == config.ADMIN:
        await message.answer(f"Привет <b>{message.from_user.first_name}</b> выбери что тебя интересует", reply_markup=kb_start)
    else:
        pass


@dp.callback_query()
async def hand(callback: CallbackQuery):
    await call(callback)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())