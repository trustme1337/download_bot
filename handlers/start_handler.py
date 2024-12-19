from aiogram import types
from aiogram.types import Message

async def start_command(message: Message):
    await message.reply("Привет! Отправь мне URL, и я скачаю файл для тебя.")
