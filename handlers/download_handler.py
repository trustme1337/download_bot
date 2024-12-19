import os
from aiogram import types
from aiogram.types import FSInputFile
from aiogram import Bot
from config import TEMP_FOLDER
from utils.downloader import download_file

async def download_file_handler(message: types.Message, bot: Bot):
    url = message.text.strip()

    # Проверяем, что это URL
    if not (url.startswith("http://") or url.startswith("https://")):
        await message.reply("Пожалуйста, отправьте действительный URL.")
        return

    # Генерируем имя временного файла
    file_name = os.path.join(TEMP_FOLDER, url.split("/")[-1] or "downloaded_file")

    await message.reply("Скачиваю файл, подождите...")

    # Скачиваем файл
    if await download_file(url, file_name):
        # Отправляем файл обратно пользователю
        file = FSInputFile(file_name)
        await bot.send_document(chat_id=message.chat.id, document=file)

        # Удаляем временный файл
        if os.path.exists(file_name):
            os.remove(file_name)
    else:
        await message.reply("Не удалось скачать файл.")
