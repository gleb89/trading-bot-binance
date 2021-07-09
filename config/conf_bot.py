from aiogram import Bot, Dispatcher, executor, types

from .settings import settings

API_TOKEN = settings.api_token

# Configure logging


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)