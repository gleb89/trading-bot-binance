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