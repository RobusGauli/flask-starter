# -*- coding: utf-8 -*-
"""
    app
    ~~~~~
    This module initializes flask app instance.
    Registers blueprints.
"""
from flask import Flask

from config import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from app.models import Base


class Sqlalchemy:

    def __init__(self, base):
        self.base = base
        self.db_url = None
        self.engine = None

    def create_engine(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        return self.engine

    def migrate(self):
        pass

    def start(self):
        self.base.metadata.create_all(self.engine)


def create_app(flask_config='development'):
    """Creates and returns app instance."""
    app = Flask(__name__)

    app.config.from_object(config[flask_config])
    sqlalchemy = Sqlalchemy(Base)
    sqlalchemy.create_engine(app.config['DATABASE_URL'])
    sqlalchemy.start()
    sqlalchemy.migrate()
    # Bluprints registration
    from app.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
