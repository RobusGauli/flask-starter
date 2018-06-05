# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""
    config
    ~~~~~
    Configuration values for different environments.
"""

import os

from lib import ConfigBase


class Config(ConfigBase):
    """
        Base Configuration.
    """
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
    """
        Test Environment Configuration
    """
    __name__ = 'test'

    DEBUG = True
    TESTING = True
    SECRET_KEY = 'testing secret key'
    DATABASE_URL = os.getenv(
        'TEST_DATABASE_URL',
        'sqlite:///'
    )


class DevelopmentConfig(Config):
    """
        Development Environment Configuration
    """
    __name__ = 'development'

    DEBUG = True
    DATABASE_URL = os.getenv(
        'DEV_DATABASE_URL',
        'sqlite:///path/to/dev/database'
    )


class ProductionConfig(Config):
    """
        Production Environment Configuration.
    """
    __name__ = 'production'

    SECRET_KEY = 'productionsecretkey'
    DEBUG = False
    DATABASE_URL = os.getenv(
        'PROD_DATABASE_URL',
        'postgres://path/to/prod/database'
    )


class UnixConfig(ProductionConfig):
    """
        Unix Environment Configuration.
    """
    __name__ = 'unix'


# pylint: disable=invalid-name
config = ConfigBase.create_config()
