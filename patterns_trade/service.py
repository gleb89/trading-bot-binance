from repositories.deal import Deal
from repositories.user import User
from binance_box.orders import get_balance
from crud.user import get_db


async def result_summ_token_for_trade(user_id, price_token):
    user = await User.objects.prefetch_related(
                    'user_deal'
                    ).get_or_none(
                    user_id=user_id
                    )

    procent = user.user_deal[0].procent_for_trade
    proc_100 = get_balance() # наш баланс в usdt
    one_proc = proc_100/100 # один процент
    
    result_summ_for_trade = one_proc* procent
        # - сумма выделенная  для торговли полученная отнимаем 5 что бы без косяков
    summ_token_for_trade = result_summ_for_trade/round(float(price_token[4]),3) # сумма токенов для ордера
    return summ_token_for_trade