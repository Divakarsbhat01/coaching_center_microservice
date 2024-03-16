import os
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    upstatus:str
    MONGO_connection_url:str
    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()
