from dotenv import load_dotenv
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 


load_dotenv()

TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("""\n
Привет🖐️ Ты запустил сигна_бот
Этот бот позволит тебе создать свое изображение с текстом⚡                         """)
    




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())