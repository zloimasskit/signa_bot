from dotenv import load_dotenv
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram import F
from image import image
load_dotenv()
TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="создать изображение")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("""\n
Привет🖐️ Ты запустил сигна_бот
Этот бот позволит тебе создать свое изображение с текстом⚡                         """, reply_markup=keyboard)
    
@dp.message(F.text.lower() == "создать изображение")
async def wit(message: types.Message):
    kb = [[types.KeyboardButton(text="трамп")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.reply("выбери персонажа", reply_markup=keyboard)

@dp.message(F.text.lower() == "трамп")
async def trum(message :types.Message):
    await message.answer("введи текст")    



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())