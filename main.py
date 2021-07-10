import logging
from aiogram import Bot, Dispatcher, executor, types
from config.conf_bot import bot
import asyncio


# from message.start import *
from message.handler import *
from message.callback import *
from repositories import user, deal
from config.database import metadata, engine, database


metadata.create_all(engine)

logging.basicConfig(level=logging.INFO)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    