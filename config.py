from starlette.config import Config

config = Config(".env")

GITHUB_URL = config("GITHUB_URL", cast=str)
DB_HOST = config("DB_HOST", cast=str)
DB_PORT = config("DB_PORT", cast=str)
DB_NAME = config("DB_NAME", cast=str)
DB_USER_NAME = config("DB_USER_NAME", cast=str)
DB_USER_PASSWORD = config("DB_USER_PASSWORD", cast=str)
