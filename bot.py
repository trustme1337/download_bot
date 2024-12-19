import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import BOT_TOKEN
from handlers.start_handler import start_command
from handlers.download_handler import download_file_handler

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчики
dp.message.register(start_command, Command("start"))
dp.message.register(download_file_handler)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
