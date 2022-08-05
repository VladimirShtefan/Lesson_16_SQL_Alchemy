from app.configs.path import DEV_DATA_BASE_DIR


class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DEV_DATA_BASE_DIR}'
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'

