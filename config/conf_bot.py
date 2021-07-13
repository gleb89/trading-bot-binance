from aiogram import Bot, Dispatcher, executor, types

from .settings import settings
import telebot



API_TOKEN = settings.api_token_telegramm
bot_not_async  = telebot.TeleBot(API_TOKEN , parse_mode=None)
# Configure logging


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)