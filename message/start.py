from aiogram import  executor, types


from config.conf_bot import dp
from crud.user import create_user

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):

#     """
#     Старт
#     """
    
#     await create_user(message.chat.id)
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton(text='Мои сделки', callback_data=1))
#     keyboard = types.ReplyKeyboardMarkup(True)
#     keyboard.row('Мои сделки', 'Добавить сделку')
#     await message.reply(f'Привет!{message.from_user.first_name}', reply_markup = keyboard)


