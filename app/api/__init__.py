# -*- coding: utf-8 -*-
"""
    api
    ~~~~~
    This module creates a bluprint and imports the handlers.
"""
from flask import Blueprint
# pylint: disable=invalid-name
api_blueprint = Blueprint('api', __name__)
# pylint: disable=wrong-import-position
from app.api import users  # noqa
