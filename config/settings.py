import os


from dotenv import load_dotenv
from pydantic import BaseSettings




class Settings(BaseSettings):

    """
    Хранит в себе данные настроек с валидацией 
    Pydantic
    """
    api_token_telegramm:str = None
    postgres_db:str = None
    postgres_user:str = None
    postgres_password:str = None
    binance_key:str = None
    binance_secret_key:str = None

    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()