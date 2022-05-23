import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot
import media


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=message.chat.id, text="Хорошо")

async def go():
    photo = open('media/sh.jpg', 'rb')
    print(photo)
    await bot.send_photo(chat_id=chat_id, photo=photo, caption="Поехали на шашлыки!!!")


async def scheduler():
    # aioschedule.every().day.at('22:17').do(go)
    aioschedule.every().day.at("22:20").do(go)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)