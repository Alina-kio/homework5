from aiogram import types, Dispatcher
from config import bot, dp


async def start(message: types.Message):
    await message.answer(f"Hi, my friend {message.from_user.full_name}")


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
