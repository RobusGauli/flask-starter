# -*- coding: utf-8 -*-
from flask import jsonify

from app.api import api_blueprint as api

@api.route('/users', methods=['GET'])
def get_users():
	_mock_data = {
		'name': 'test_user'
	}

  return jsonify(_mock_data)