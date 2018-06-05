# -*- coding: utf-8 -*-
"""
    api.users
    ~~~~~
    Handlers for user endpoint
"""
from flask import jsonify

from app.api import api_blueprint as api


@api.route('/users', methods=['GET'])
def get_users():
    """Returns list of users"""
    return jsonify({
        'name': 'test_user'
    })
