import asyncio
from time import sleep

from crud.user import get_bool_trade_trhread
from patterns_trade import ema_ribbon

async def start_ema(tiker,interval,user_id):
    deal_t = await get_bool_trade_trhread(str(user_id))
    ema =  ema_ribbon.EmaRibbon()
    while deal_t:
        await ema.logicks_price_in_ema(tiker, interval, user_id)
        if interval == '5m':
            sleep(300)
        elif interval == '15m':
            sleep(1200)
        elif interval == '30m':
            sleep(1800)
        elif interval == '1h':
            sleep(3600)
        elif interval == '4h':
            sleep(14400)
        deal_t = await get_bool_trade_trhread(str(user_id))

def thread_function(tiker,interval,user_id):
    asyncio.run(start_ema(tiker,interval,user_id))