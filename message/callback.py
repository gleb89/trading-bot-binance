from aiogram import  types

from config.conf_bot import dp
from crud.user import get_bool_trade, add_interval_time, add_para_trade, get_db


@dp.message_handler()
async def echo_all(message:types.Message):
    if message.text[:10] == 'Мои сделки':
        mess = await get_bool_trade(str(message.chat.id))
        await message.answer(mess)
    elif message.text == 'Добавить сделку 💱':
        markup = types.InlineKeyboardMarkup()
        btn_5m = types.InlineKeyboardButton(text='5m', callback_data="5m")
        btn_15m = types.InlineKeyboardButton(text='15m', callback_data="15m")
        btn_30m = types.InlineKeyboardButton(text='30m', callback_data="30m")
        btn_1h = types.InlineKeyboardButton(text='1h', callback_data="1h")
        btn_4h = types.InlineKeyboardButton(text='4h', callback_data="4h")
        markup.add(btn_5m,btn_15m,btn_30m,btn_1h,btn_4h)
        await message.answer("Выберите интервал баров для торговли.", reply_markup = markup)

async def get_buton_interval(call):
    markup = types.InlineKeyboardMarkup()
    btn_dashusdt= types.InlineKeyboardButton(text='dashusdt', callback_data="dashusdt")
    btn_btcusdt = types.InlineKeyboardButton(text='btcusdt', callback_data="btcusdt")
    btn_ethusdt = types.InlineKeyboardButton(text='ethusdt', callback_data="ethusdt")
    btn_icpusdt = types.InlineKeyboardButton(text='icpusdt', callback_data="icpusdt")
    btn_chrusdt = types.InlineKeyboardButton(text='chrusdt', callback_data="chrusdt")
    markup.add(btn_dashusdt,btn_btcusdt,btn_ethusdt,btn_icpusdt,btn_chrusdt)
    await add_interval_time(str(call["from"]["id"]),str(call.data))
    await call.message.answer("Выберите пару для торгов.", reply_markup = markup)

@get_db
async def get_buton_adds(call):
    markup = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Подвердить', callback_data="yes")
    no = types.InlineKeyboardButton(text='Отменить', callback_data="no")
    markup.add(yes,no)
    data_trade = await add_para_trade(str(call["from"]["id"]),str(call.data))
    interval = data_trade['interval']
    para = data_trade['deal_symbol']
    await call.message.answer(f'Условие торгов для бота : таймфрейм {interval} ,пара : {para}', reply_markup = markup)

@dp.callback_query_handler()
async def callback_inline(call:types.CallbackQuery):
    if call.data in ['5m','15m','30m','1h','4h','1h',]:
        await get_buton_interval(call)

    if call.data in ["1","2","chrusdt","dashusdt","btcusdt","ethusdt","icpusdt"]:
        markup = await get_buton_adds(call)

    if call.data == "yes" :
        await call.message.answer("Запущено")
    if call.data == "no" :
        await call.message.answer("Отменено")