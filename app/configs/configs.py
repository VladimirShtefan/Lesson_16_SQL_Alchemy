from pathlib import Path


class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATABASE_DIR = BASE_DIR.joinpath('data_base')
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_DIR}/development.db'
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
    SQLALCHEMY_ECHO = False
