import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    DB_USER = os.getenv(f'DB_USER_DEV', 'admin')
    DB_PASSWORD = os.getenv(f'DB_PASSWORD_DEV', 'admin1234')
    DB_NAME = os.getenv(f'DB_NAME_DEV', 'flask')
    DB_HOST = os.getenv(f'DB_HOST_DEV', 'localhost')
    DB_PORT = os.getenv(f'DB_PORT_DEV', '5432')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_USER = os.getenv(f'DB_USER_TEST', 'admin')
    DB_PASSWORD = os.getenv(f'DB_PASSWORD_TEST', 'admin1234')
    DB_NAME = os.getenv(f'DB_NAME_TEST', 'flask_test')
    DB_HOST = os.getenv(f'DB_HOST_TEST', 'localhost')
    DB_PORT = os.getenv(f'DB_PORT_TEST', '5432')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
