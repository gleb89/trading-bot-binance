from aiogram import  types
from crud.user import (
                        add_interval_time,
                        add_para_trade,
                        get_db,
                        add_proc_trade
                    )

async def get_buton_interval(call):

    """
    Вывод кнопок торговой пары,если интервал торговли выбран
    """

    markup = types.InlineKeyboardMarkup()
    btn_dashusdt= types.InlineKeyboardButton(text='dashusdt', callback_data="dashusdt")
    btn_btcusdt = types.InlineKeyboardButton(text='btcusdt', callback_data="btcusdt")
    btn_ethusdt = types.InlineKeyboardButton(text='ethusdt', callback_data="ethusdt")
    btn_icpusdt = types.InlineKeyboardButton(text='icpusdt', callback_data="icpusdt")
    btn_chrusdt = types.InlineKeyboardButton(text='chrusdt', callback_data="chrusdt")
    btn_keepusdt = types.InlineKeyboardButton(text='keepusdt', callback_data="keepusdt")
    btn_blzusdt = types.InlineKeyboardButton(text='blzusdt', callback_data="blzusdt")
    markup.add(
        btn_dashusdt,
        btn_btcusdt,
        btn_ethusdt,
        btn_icpusdt,
        btn_chrusdt,
        btn_keepusdt,
        btn_blzusdt
        )
    await add_interval_time(str(call["from"]["id"]),str(call.data))
    await call.message.answer("Выберите пару для торгов.", reply_markup = markup)


@get_db
async def get_buton_adds(call):

    """
    Вывод подверждения запуска отслеживания точки входа в сделку
    Запускает работу алгоритма поиска точки входа на выбранном таймфрейме
    """

    markup = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Подвердить', callback_data="yes")
    no = types.InlineKeyboardButton(text='Отменить', callback_data="no")
    markup.add(yes,no)
    data_trade = await add_proc_trade(str(call["from"]["id"]),int(call.data))
    interval = data_trade['interval']
    para = data_trade['deal_symbol']
    proc = data_trade['procent_for_trade']
    await call.message.answer(
        f'Условие торгов для бота : \n таймфрейм - {interval} \n пара : {para} \n процент от депозита: {proc} %', 
        reply_markup = markup
        )

async def get_buton_adds_proc(call):
    markup = types.InlineKeyboardMarkup()
    proc_5 = types.InlineKeyboardButton(text='5%', callback_data="5%")
    proc_10 = types.InlineKeyboardButton(text='10%', callback_data="10")
    proc_20 = types.InlineKeyboardButton(text='20%', callback_data="20")
    proc_30 = types.InlineKeyboardButton(text='30%', callback_data="30")
    proc_40 = types.InlineKeyboardButton(text='40%', callback_data="40")
    proc_50 = types.InlineKeyboardButton(text='50%', callback_data="50")
    proc_60 = types.InlineKeyboardButton(text='60%', callback_data="60")
    proc_70 = types.InlineKeyboardButton(text='70%', callback_data="70")
    proc_80 = types.InlineKeyboardButton(text='80%', callback_data="80")
    proc_90 = types.InlineKeyboardButton(text='90%', callback_data="90")
    proc_100 = types.InlineKeyboardButton(text='100%', callback_data="100")
    

    markup.add(
        proc_5,proc_10,proc_20,proc_30,proc_40,proc_50, proc_80,proc_60,proc_70,proc_90,proc_100,
        )
    data_trade = await add_para_trade(str(call["from"]["id"]),str(call.data))

    await call.message.answer(
        f'Выберите % от депозита для торговли на сделку', 
        reply_markup = markup
        )