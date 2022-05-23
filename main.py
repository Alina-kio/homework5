import asyncio
from aiogram.utils import executor
from config import dp
from hendlers import noti, client
import logging

async def on_startup(_):
    asyncio.create_task(noti.scheduler())


client.register_handler_client(dp)
noti.register_handler_notification(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
