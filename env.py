# -*- coding: utf-8 -*-
"""
    Loading environment variables for application.
"""
import os
import sys

from dotenv import load_dotenv


def initialize_env():
    env_dir_path = os.path.abspath(os.path.curdir)
    env_path = os.path.join(env_dir_path, '.env')
    if not os.path.exists(env_path):
        raise FileNotFoundError('Environment file does not exists.')
    load_dotenv(os.path.join(env_path, '.env'))
