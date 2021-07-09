from repositories import user, deal
from config.database import database

def get_db(func):
    db = database
    async def connect_db(*args, **kwargs):
        await db.connect()
        await func(*args, **kwargs)
        await db.disconnect()
    return connect_db

@get_db
async def create_user(text):
    user_pk = await user.User.objects.prefetch_related('user_deal').get_or_none(user_id=text)
    if user_pk:
        pass
    else:
        new_user = user.User(user_id=text)
        await new_user.save()
        deal_user = await deal.Deal.objects.create(owner=new_user,deal_symbol='',id_deal_proces='',interval='')
        return user


async def get_bool_trade(user_id):
    await database.connect()
    user_pk = await user.User.objects.prefetch_related('user_deal').get_or_none(user_id=user_id)
    await database.disconnect()
    if user_pk.user_deal[0].deal_true == True:
        return f'торговая пара:{user_pk.user_deal[0].deal_symbol}'
        
    else:
        return "нет сделок"

@get_db
async def add_interval_time(user_id, time_interval):
    user_pk = await user.User.objects.prefetch_related('user_deal').get_or_none(user_id=user_id)
    deal_user = await deal.Deal.objects.get_or_none(owner=user_pk)
    await deal_user.update(interval=time_interval)


async def add_para_trade(user_id, para):
    user_pk = await user.User.objects.prefetch_related('user_deal').get_or_none(user_id=user_id)
    deal_user = await deal.Deal.objects.get_or_none(owner=user_pk)
    deals = await deal_user.update(deal_symbol=para)
    return {"interval":deals.interval,
            "deal_symbol":deals.deal_symbol
            }

    
    