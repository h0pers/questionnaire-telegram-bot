from aiogram import types, Router
from bot.middleware.db_updates import CollectData, CollectCallbackData

other_router = Router()

other_router.message.middleware(CollectData())
other_router.callback_query.middleware(CollectCallbackData())
