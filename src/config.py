from starlette.config import Config
from starlette.datastructures import Secret


env = Config(".env")

SECRET_KEY = env("SECRET_KEY", cast=Secret)

DB_USER = env("DB_USER", cast=str)
DB_PASSWORD = env("DB_PASSWORD", cast=Secret)
DB_HOST = env("DB_HOST", cast=str, default="db")
DB_PORT = env("DB_PORT", cast=str, default="5432")
DB_NAME = env("DB_NAME", cast=str)
