import ormar
import pydantic

from .base import BaseMeta




class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True)
    user_id:str = ormar.String(max_length=50)