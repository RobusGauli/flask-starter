# -*- coding: utf-8 -*-
from flask import Flask

from config import config


def create_app(flask_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[flask_config])

    # Bluprints registration
    from app.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
