from typing import Optional


import ormar 
from .user import User
from .base import BaseMeta





class Deal(ormar.Model):
    class Meta(BaseMeta):
        tablename = "deal traide"

    id: int = ormar.Integer(primary_key=True)
    deal_true:bool = ormar.Boolean(default=False)
    owner: User = ormar.ForeignKey(User, related_name="user_deal")
    deal_symbol: str = ormar.String(max_length=50,null=True)
    interval: str = ormar.String(max_length=100,null=True)
    id_deal_proces: str = ormar.String(max_length=100,null=True)