# -*- coding: utf-8 -*-
import os

from lib import ConfigBase

class Config(ConfigBase):
    DEBUG = False 
    TESTING = False
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'default secret key'
    )
    DATABASE_URL = os.getenv(
        'DATABASE',
        'sqlite:///default database url'
    )


class TestingConfig(Config):
    __name__ = 'test'

    DEBUG = True
    TESTING = True
    SECRET_KEY='testing secret key'
    DATABASE_URL = os.getenv(
        'TEST_DATABASE_URL',
        'sqlite:///'
    )

class DevelopmentConfig(Config):
    __name__ = 'development'

    DEBUG = True
    DATABASE_URL = os.getenv(
        'DEV_DATABASE_URL',
        'sqlite:///path/to/dev/database'
    )

class ProductionConfig(Config):
    __name__ = 'production'

    SECRET_KEY = 'productionsecretkey'
    DEBUG = False
    DATABASE_URL = os.getenv(
        'PROD_DATABSE_URL',
        'postgres://path/to/prod/database'
    )

class UnixConfig(ProductionConfig):
    __name__ = 'unix'
    
config = ConfigBase.create_config()
