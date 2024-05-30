from starlette.config import Config


env = Config(".env")

SECRET_KEY = env("SECRET_KEY", cast=str)

DB_USER = env("DB_USER", cast=str)
DB_PASSWORD = env("DB_PASSWORD", cast=str)
DB_HOST = env("DB_HOST", cast=str, default="db")
DB_PORT = env("DB_PORT", cast=str, default="5432")
DB_NAME = env("DB_NAME", cast=str)
