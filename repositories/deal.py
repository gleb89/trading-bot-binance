from typing import Optional


import ormar 
from .user import User
from .base import BaseMeta



class Deal(ormar.Model):

    """
    Таблица трейда привязанного к юсеру,
    {deal_true }- торговый процес по поиску точки входа
    True -процес работает в фоне,False -нет процесса запущенного
    {owner} - юсер трейда
    {deal_symbol} - торговая пара выбранная юсером
    {interval} -таймфрейм для торгов
    {id_deal_proces }-есть текущая сделка или нет
    """
    
    class Meta(BaseMeta):
        tablename = "deal traide"

    id: int = ormar.Integer(primary_key=True)
    deal_true:bool = ormar.Boolean(default=False)
    owner: User = ormar.ForeignKey(User, related_name="user_deal")
    deal_symbol: str = ormar.String(max_length=50,null=True)
    interval: str = ormar.String(max_length=100,null=True)
    id_deal_proces:bool = ormar.Boolean(default=False)
    