from decimal import Decimal



from .base import Base_binance
from repositories.deal import Deal
from repositories.user import User

from config.conf_bot import  bot_not_async 
from config.database import database
from crud.user import get_db



class EmaRibbon(Base_binance):

    def __init__(self) -> None:
        super().__init__()


    async def create_ema_price(self, data,num_ema):
        return sum(
            [Decimal(price_close[4]) for price_close in data]
            )/num_ema



    async def get_bars_all(self, pars, interval):
        
        self.session.headers.update(self.headers)
        bars_price_interval = (
            'https://api.binance.com/api/v3/klines?symbol='
            f'{pars.upper()}'
            '&interval='
            f'{interval}'
            )
       
        price_url = (
                    'https://api.binance.com/api/v3/ticker/price?symbol='
                    f'{pars.upper()}'
                    )
        data_price = self.session.get(price_url).json()
        data = self.session.get(bars_price_interval).json()
        bars_4_end = [Decimal(price_close[4]) for price_close in data[-5:]]
        data_for_atr = data[-10:].copy()
        data_for_atr.pop()
        atr = sum(
            [Decimal(ind_data[2])-Decimal(ind_data[3]
            ) 
            for ind_data in data_for_atr])/len(data_for_atr)

        return atr, bars_4_end, dict(
        data_price = data_price ,
        ema55 = await self.create_ema_price(data[-55:], 55),
        ema50 = await self.create_ema_price(data[-50:], 50),
        ema45 = await self.create_ema_price(data[-45:], 45),
        ema40 = await self.create_ema_price(data[-40:], 40),
        ema35 = await self.create_ema_price(data[-35:], 35),
        ema30 = await self.create_ema_price(data[-30:], 30),
        ema25 = await self.create_ema_price(data[-25:], 25),
        ema21 = await self.create_ema_price(data[-21:], 21),  
        )

    @get_db
    async def logicks_price_in_ema(self, tiker, interval, chat_id):
        atr ,bars_4_end, bars_data = await self.get_bars_all(
                                                tiker, interval
                                                )
        
        #ema ribbon в отрицательных значениях
        ema_rib_negative = (
                        bars_data['ema21'] < bars_data['ema55']
                        )
        # #ema ribbon в положительных значениях
        ema_rib_positive = (
                        bars_data['ema21'] > bars_data['ema55']
                        )
        if ema_rib_negative:
            #предыдущие 3 бара ниже ma55 ,а последняя закрылась выше ma55
            if (
                bars_4_end[0] < bars_data['ema55']
                and bars_4_end[1] < bars_data['ema55']
                and bars_4_end[2] < bars_data['ema55']
                and bars_4_end[3] > bars_data['ema55']
                ):
                bars_4_end.pop()
                stop_position = bars_data['ema55'] - atr
                
                bot_not_async.send_message(
                    chat_id,
                    'Покупка' 
                    f'{bars_4_end[4]}'
                    'stop'
                    f'{stop_position}'
                    )
                
                user = await User.objects.prefetch_related(
                    'user_deal'
                    ).get_or_none(
                    user_id=chat_id
                    )
                deal = await Deal.objects.get(owner=user)
                await deal.update(id_deal_proces=True,deal_true=False)
               
            
            else:
                # print(chat_id)
             
                bot_not_async.send_message(chat_id,'нет точки входа в long')
        elif ema_rib_positive:
            #предыдущие 3 бара выше ma55 ,а последняя закрылась ниже ma55
            if (
                bars_4_end[0] > bars_data['ema55']
                and bars_4_end[1] > bars_data['ema55']
                and bars_4_end[2] > bars_data['ema55']
                and bars_4_end[3] < bars_data['ema55']
                ):
     
                stop_position = bars_data['ema21'] + atr
                bot_not_async.send_message(
                    chat_id,
                    'Шорт позиция' 
                    f'{bars_4_end[4]}'
                    'stop'
                    f'{stop_position}'
                    )
                user = await User.objects.prefetch_related(
                    'user_deal'
                    ).get_or_none(
                    user_id=chat_id
                    )
                deal = await Deal.objects.get(owner=user)
                await deal.update(id_deal_proces=True,deal_true=False)
                
            else:
                bot_not_async.send_message(chat_id,'нет точки входа в шорт')
        else:
            bot_not_async.send_message(chat_id,'хз')