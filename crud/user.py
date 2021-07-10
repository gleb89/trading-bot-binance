from repositories import user, deal
from config.database import database



def get_db(func):

    """
    Декоратор для включения и
    отключения подключения к базе данных
    """

    db = database
    async def connect_db(*args, **kwargs):
        await db.connect()
        bool_func = await func(*args, **kwargs)
        await db.disconnect()
        return bool_func
    return connect_db



@get_db
async def create_user(text):
    """
    Возвращает пользователя,
    при его отсутсвии в бд создает нового
    """
    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=text)
    if user_pk:
        pass
    else:
        new_user = user.User(user_id=text)
        await new_user.save()
        deal_user = await deal.Deal.objects.create(
            owner=new_user,deal_symbol='',interval=''
            )
        return user


@get_db
async def get_bool_trade(user_id):

    """
    Определяет в каком статусе сделка или торговый процес ,
    Возвращает статус сделки или торгового процесса
    """

    otmena = None
    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=user_id)

    if user_pk.user_deal[0].deal_true == True:
        otmena = True
        return otmena, ('идет поиск точки входа!\n торговая пара:\n'
        f'{user_pk.user_deal[0].deal_symbol} \n'
        'на интервале \n'
        f'{user_pk.user_deal[0].interval}'
        )

    elif user_pk.user_deal[0].deal_true == False and\
        user_pk.user_deal[0].id_deal_proces == True:
        return otmena(
            'сделка :\n '
            f'{user_pk.user_deal[0].deal_symbol}\n'
            'на интервале \n '
            f'{user_pk.user_deal[0].interval} '
        )

    else:
        return otmena, 'нет  ни поиска точки входа, ни сделок'   



@get_db
async def add_interval_time(user_id, time_interval):

    """
    Добавляет в таблицу сделки юсера интервал
    для торгового процесса поиска точки входа
    """

    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=user_id)
    deal_user = await deal.Deal.objects.get_or_none(owner=user_pk)
    await deal_user.update(interval=time_interval)

async def get_bool_trade_trhread(user_id):

    """
    Выполняет проверку есть ли торговый процесс поиска
    точки входа у сделки юсера
    Выводит True или False 
    """

    await database.connect()
    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=user_id)
    await database.disconnect()

    if user_pk.user_deal[0].deal_true == True:
        return True 
    else:
        return False



@get_db
async def add_deal_trade(user_id, deal_t):

    """
    Добавляет статус True в поле user_deal в таблице deal 
    Обращается к данной функции ,если в режиме поиска точки входа 
    находит точку входа и входит в сделку
    """

    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=user_id)
    
    deal_user = await deal.Deal.objects.get_or_none(owner=user_pk)
    deals = await deal_user.update(deal_true=deal_t)
    return deals.interval, deals.deal_symbol
    


async def add_para_trade(user_id, para):

    """
    Добавляет в таблицу deal привязанной к юсеру
    символ торговой пары для торговли
    """
    
    user_pk = await user.User.objects.prefetch_related(
        'user_deal'
        ).get_or_none(user_id=user_id)
    deal_user = await deal.Deal.objects.get_or_none(owner=user_pk)
    deals = await deal_user.update(deal_symbol=para)
    return {"interval":deals.interval,
            "deal_symbol":deals.deal_symbol
            }




    