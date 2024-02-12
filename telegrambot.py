import aiogram
from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from task import get_photo_urls
from aiogram.types import InputFile
# from aiogram.types import Photo
import asyncio
import requests
import random

bot = Bot(token='6319103400:AAEuv0bl6KFALVpDngLFT2wHcOxq5mVSRto')
dp = Dispatcher()


async def send_random_photo(message):
    photo_urls = get_photo_urls()  # Get a list of photo URLs
    if photo_urls:
        random_photo_url = random.choice(photo_urls)  # Select a random photo URL
        await bot.send_photo(message.chat.id, photo=random_photo_url)
    else:
        await message.answer("Failed to retrieve photos.")
@dp.message(CommandStart())
async def handle_photo(message: Message):
    await send_random_photo(message)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())