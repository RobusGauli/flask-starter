# -*- coding: utf-8 -*-
"""
    app
    ~~~~~
    This module initializes flask app instance.
    Registers blueprints.
"""
from flask import Flask

from config import config
from lib import FlaskSqlSession

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from app.models import Base
from lib.flask_sql_session import dbsession


def create_app(flask_config='development'):
    """Creates and returns app instance."""
    app = Flask(__name__)

    app.config.from_object(config[flask_config])
    print(app.config['ENV'])
    # Bluprints registration
    from app.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # create and session factory from the engine and attach
    # it app instance as an attribute
    engine = create_engine(app.config['DATABASE_URL'])
    session_factory = sessionmaker(engine, autocommit=False, autoflush=False)

    # proxy dbsession using flask_sql_session
    FlaskSqlSession(session_factory, app)
    return app


__all__ = ['create_app', 'Base', 'dbsession']
