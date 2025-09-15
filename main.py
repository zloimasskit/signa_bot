from dotenv import load_dotenv
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from image import image
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()
TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

class Stater(StatesGroup):
    choosing_text = State()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [[types.KeyboardButton(text="создать изображение")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        "Привет🖐️ Ты запустил сигна_бот!\nЭтот бот позволит тебе создать своё изображение с текстом⚡",
        reply_markup=keyboard
    )

@dp.message(F.text.lower() == "создать изображение")
async def wit(message: types.Message):
    kb = [[types.KeyboardButton(text="трамп")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.reply("выбери персонажа", reply_markup=keyboard)

@dp.message(F.text.lower() == "трамп")
async def trum(message: types.Message, state: FSMContext):
    await message.answer("введи текст")
    await state.set_state(Stater.choosing_text)

@dp.message(Stater.choosing_text)
async def proccess(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(text=name)

    img_buffer = image.generate("sda", text=name)  # должен возвращать BytesIO
    await message.answer_photo(
        types.BufferedInputFile(img_buffer.getvalue(), filename="image_with_text.jpg")
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
