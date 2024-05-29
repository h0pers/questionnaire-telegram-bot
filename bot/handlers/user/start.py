from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.config import MessageText
from bot.keyboards.inline.start import start_inline_markup

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=MessageText.WELCOME, reply_markup=start_inline_markup.get_markup())
