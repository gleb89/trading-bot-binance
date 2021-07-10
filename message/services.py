from aiogram import  types
from crud.user import (
                        add_interval_time,
                        add_para_trade, get_db
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
    data_trade = await add_para_trade(str(call["from"]["id"]),str(call.data))
    interval = data_trade['interval']
    para = data_trade['deal_symbol']
    await call.message.answer(
        f'Условие торгов для бота : \n таймфрейм - {interval} \n пара : {para}', 
        reply_markup = markup
        )