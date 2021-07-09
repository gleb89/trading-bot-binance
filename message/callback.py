from aiogram import  types

from config.conf_bot import dp

@dp.message_handler()
async def echo_all(message:types.Message):
    if message.text == 'Мои сделки 💸':
        mess = 'dct p,c'
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
    # url = f'http://localhost:8000/ema_ribbon_data/time?user_id={call.from_user.id}&interval={call.data}'
    # data = session.get(url)
    await call.message.answer("Выберите пару для торгов.", reply_markup = markup)


async def get_buton_adds(call):
    markup = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Подвердить', callback_data="yes")
    no = types.InlineKeyboardButton(text='Отменить', callback_data="no")
    markup.add(yes,no)
    
    # url = f'http://localhost:8000/user/?user_id={call.from_user.id}'
    # data = session.get(url)
    # response_data = data.json()
    # url_symvol = f'http://localhost:8000/ema_ribbon_data/para?user_id={call.from_user.id}&symbol={call.data}'
    # data_symvol = session.get(url_symvol)
    
    # interval = response_data['user_deal'][0]['interval']
    await call.message.answer(f'Условие торгов для бота : таймфрейм ,пара : ', reply_markup = markup)

@dp.callback_query_handler()
async def callback_inline(call:types.CallbackQuery):
    if call.data == '5m':
        await get_buton_interval(call)
    if call.data == '15m':
        await get_buton_interval(call)
    if call.data == '30m':
        await get_buton_interval(call)
    if call.data == '1h':
        await get_buton_interval(call)
    if call.data == '4h':
        await get_buton_interval(call)
    if call.data == "1" :
        markup = await get_buton_adds(call)
    if call.data == "2" :
        markup = await get_buton_adds(call) 
    if call.data == "chrusdt" :
        markup = await get_buton_adds(call)
    if call.data == "dashusdt" :
        markup = await get_buton_adds(call)
    if call.data == "btcusdt" :
        markup = await get_buton_adds(call)
    if call.data == "ethusdt" :
        markup = await get_buton_adds(call)
    if call.data == "icpusdt" :
        markup = await get_buton_adds(call)
    if call.data == "yes" :
        # url = f'http://localhost:8000/ema_ribbon_data/?user_id={call.from_user.id}'
        # data = session.get(url)
        await call.message.answer("Запущено")
    if call.data == "no" :
        await call.message.answer("Отменено")