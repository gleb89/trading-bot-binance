from binance.client import Client
from decimal import Decimal
import math
from config.settings import settings
KEY = settings.binance_key
SECRET = settings.binance_secret_key

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

import decimal

def reverce_lot_size(step_size,count_token):
    precision = int(round(-math.log(step_size, 10), 0))
    quantity = float(round(count_token, precision))
    return quantity


def get_size(symbol):
    for i in client.get_exchange_info()['symbols']:
        if i['symbol'] == symbol:
            for i in i['filters']:
                if i['filterType'] == 'LOT_SIZE':
                    step_size = float(i['stepSize'])
                    return step_size

def orders_for_trade(symbol, stop_price, count_token):
    try:

        step_size = get_size(symbol)
        quantity  = reverce_lot_size(step_size,count_token)
        market_order = client.order_market_buy(
        symbol=symbol,
        quantity=quantity 
        )
        
        count_for_stop = float(market_order['fills'][0]['qty']) - float(market_order['fills'][0]['commission'])
        quantity  = reverce_lot_size(step_size,count_for_stop)
        order = client.create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=ORDER_TYPE_STOP_LOSS_LIMIT,
        quantity=quantity,
        timeInForce=TIME_IN_FORCE_GTC,
        price=str(round(stop_price, 2)),
        stopPrice=str(round(stop_price, 2))
        )
        return True
    except Exception as e:
        print(e)
        return False

def close_position(symbol=None):
    orders_stop_for_symbol = client.get_open_orders(symbol=symbol)
    quantity_stop = orders_stop_for_symbol[0]['origQty']
    id_order = orders_stop_for_symbol[0]['orderId']
    step_size = get_size(symbol)
    quantity = reverce_lot_size(step_size,float(quantity_stop))
    result = client.cancel_order(
    symbol=symbol,
    orderId=id_order)
    order = client.order_market_sell(
    symbol=symbol.upper(),
    quantity=quantity)
