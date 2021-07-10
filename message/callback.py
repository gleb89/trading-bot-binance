import asyncio
from threading import Thread


from aiogram import  types


from config.conf_bot import dp
from crud.user import (
                        get_bool_trade,
                        get_bool_trade_trhread,
                        add_deal_trade,
                    )
from .thread import thread_function
from .services import get_buton_adds, get_buton_interval



@dp.message_handler()
async def echo_all(message:types.Message):
    """
    Отслеживание сообщений при нажатии кнопок
    под названием -мои сделки и добавить сделку.
    Выводит текущие сделки ,если они имеются
    или при нажатии добавить сделку выводит 
    (при наличии процеса поиска точки входа)
    предложение отменить проццес поиска точки входа,
    при его отсутвии предлагает выбрать таймфрем для поска точки входа
    """
    otmena_button = types.InlineKeyboardButton(
                text='Отменить торговый процесс',
                callback_data="отмена"
                )
    if message.text == 'Мои сделки 💸':
        otmena ,mess = await get_bool_trade(
                str(message.chat.id)
                )
        if otmena:
            markup = types.InlineKeyboardMarkup()
            markup.add(otmena_button)
            await message.answer(mess,reply_markup=markup, parse_mode='html')
        else:
            await message.answer(mess)
    elif message.text == 'Добавить сделку 💱':
        if await get_bool_trade_trhread(
                    str(message.chat.id)
                    ):
            markup = types.InlineKeyboardMarkup()
            markup.add(otmena_button )
            await message.answer(
                f'У вас уже запущен торговый процесс ,но сделки еще нет',
                reply_markup=markup,
                parse_mode='html'
                )
        else:
            markup = types.InlineKeyboardMarkup()
            btn_5m = types.InlineKeyboardButton(
                text='5m',
                callback_data="5m"
                )
            btn_15m = types.InlineKeyboardButton(
                text='15m',
                callback_data="15m"
                )
            btn_30m = types.InlineKeyboardButton(
                text='30m',
                callback_data="30m"
                )
            btn_1h = types.InlineKeyboardButton(
                text='1h',
                callback_data="1h"
                )
            btn_4h = types.InlineKeyboardButton(
                text='4h',
                callback_data="4h"
                )
            markup.add(
                btn_5m,btn_15m,btn_30m,btn_1h,btn_4h
                )
            await message.answer(
                "Выберите интервал баров для торговли.",
                reply_markup = markup)




@dp.callback_query_handler()
async def callback_inline(call:types.CallbackQuery):
    """
    Отслеживает нажатия кнопок
    """
    if call.data in [
        '5m',
        '15m',
        '30m',
        '1h',
        '4h',
        '1h',
        ]:
        await get_buton_interval(call)

    if call.data in [
        "1",
        "2",
        "chrusdt",
        "dashusdt",
        "btcusdt",
        "keepusdt",
        "ethusdt",
        "icpusdt",
        "blzusdt"
        ]:
        markup = await get_buton_adds(call)

    if call.data == "yes" :
        try:
            interval,symbol = await add_deal_trade(
                str(call["from"]["id"]),
                deal_t=True
                )
            user_id = str(call["from"]["id"])
            trade = Thread(
                target=thread_function,
                args=(symbol,interval,user_id,)
                )
            trade.start()
            await call.message.answer("Запущено")
        except:
            await call.message.answer(
                "Что-то пошло не так,поробуйте ещ раз!"
                )

    if call.data == "no" :
        await call.message.answer("Отменено")
    if call.data == "отмена" :
        await add_deal_trade(
            str(call["from"]["id"]),deal_t=False
            )
        await call.message.answer("Успешно отменено!")