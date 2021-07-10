import ormar
import pydantic

from .base import BaseMeta




class User(ormar.Model):

    """
    Таблица пользователей
    user_id берется из id user telegramm
    """
    
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True)
    user_id:str = ormar.String(max_length=50)