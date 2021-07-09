from aiogram import  types

from config.conf_bot import dp
from crud import user



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await user.create_user(str(message.chat.id))
    trade = await user.get_bool_trade(str(message.chat.id))
    count = ""
    if trade == "нет сделок":
        count = "0"
    else:
        count = "1"

    button_sdelki = types.KeyboardButton(f'Мои сделки {count} 💸')
    button_add_sdelka= types.KeyboardButton('Добавить сделку 💱')
    greet_kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_sdelki, button_add_sdelka)
    await message.reply(f'Привет!{message.from_user.first_name}', reply_markup = greet_kb1 )




