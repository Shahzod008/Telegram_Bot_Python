from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher
from keyboard import kb_start
from callb import handlers
import logging
import asyncio

bot = Bot(token="7198798391:AAEw7Inb0fW6kJ-WqMBKasyu69A3jGUiN2g", parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет <b>{message.from_user.first_name}</b> выбери что тебя интересует",
                         reply_markup=kb_start)


@dp.callback_query()
async def hand(callback: CallbackQuery):
    await handlers(callback)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
