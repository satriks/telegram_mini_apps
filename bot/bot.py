import asyncio
import logging
import json
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.content_type import ContentType
from aiogram.filters import  Command
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()


@dp.message(Command(commands=['play']))
async def play(message: types.Message):
    webAppInfo = types.WebAppInfo(url=os.getenv("MINI_APPS"))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='Играть', web_app=webAppInfo))
    await message.answer(text='Сиграем?', reply_markup=builder.as_markup())

@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f'<b>{data["title"]}</b>\n\n<code>{data["desc"]}</code>\n\n{data["text"]}',
                         parse_mode=ParseMode.HTML)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())