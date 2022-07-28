from dotenv import find_dotenv, load_dotenv
from os import getenv
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

if not load_dotenv(find_dotenv('.env')):
    raise Exception("Documento .env não encontrado !")

class Settings(BaseSettings):
    """
    Configurações gerais  usadas na applicação
    """
    DB_HOST: str = getenv('HOST_DB')
    DB_USER_NAME: str = getenv('USER_DB')
    DB_PASSWORD: str = getenv('PASSWORD_DB')
    DB_PORT: str = getenv('PORT_DB')
    DB_NAME: str = getenv('NAME_DB')
    API_V1_STR: str =  '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    DB_BASE_MODEL =  declarative_base()

    class config:
        case_sensitive: bool = True


settings = Settings()