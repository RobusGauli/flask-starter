# -*- coding: utf-8 -*-
"""
    flask_starter
    ~~~~~
    Entry point for flask app.
"""
import os

import flask
import cli
from app import create_app

# initiliaze environment variables
flask.cli.load_dotenv(path=os.path.join(os.path.curdir, '.env'))
# pylint: disable=invalid-name
flask_environment = os.getenv(
    'FLASK_ENV',
    'development'
)
app = create_app(flask_environment)
cli.register(app)