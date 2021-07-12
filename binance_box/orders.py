from binance.client import Client
from decimal import Decimal
KEY = 'VPWNpRRtm8J0TJ9miR6HweCqQRr4DTetW1q26tSeTLr8w9BJ0WN08QqsNpPomFZb'
SECRET = '57cWhuqtvLXG8AKSOrpGzZrM9jxEe1CDynjnHipf2XSl7cggdsWw6uap6jskyPnW'

client = Client(KEY, SECRET)
from binance.enums import *

def get_balance():
    account_spot:dict = client.get_account()
    usdt_balance = [
    ticker['free']
    for ticker in account_spot['balances']
    if ticker['asset'] == 'USDT'
    ][0]
    return round(float(usdt_balance),3)


def orders_for_trade(symbol, stop_price):
    try:

        # купить по рынку
        market_order = client.order_market_buy(
        symbol=symbol,
        quantity=1
        )
        count_for_stop = float(market_order['fills'][0]['qty']) - float(market_order['fills'][0]['commission'])
        print(market_order)
        # стоп лимит ордер
        order = client.create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=ORDER_TYPE_STOP_LOSS_LIMIT,
        quantity=round(count_for_stop, 2),
        timeInForce=TIME_IN_FORCE_GTC,
        price=str(round(stop_price, 2)),
        stopPrice=str(round(stop_price, 2))
        )
        
        return True
    except:
        return False
