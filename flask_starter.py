# -*- coding: utf-8 -*-
"""
    flask_starter
    ~~~~~
    Entry point for flask app.
"""
import os

import cli
from app import create_app
from env import initialize_env

# initiliaze environment variables
initialize_env()
# pylint: disable=invalid-name
flask_environment = os.getenv(
    'FLASK_CONFIG',
    'development'
)
app = create_app(flask_environment)
cli.register(app)
