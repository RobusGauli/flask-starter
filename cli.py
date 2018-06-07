# -*- coding: utf-8 -*-
"""
    cli
    ~~~~~
    Flask command interface.
    Usage:
        $ flask --help
        $ flask lint
        $ flask autopep
"""
import sys
import subprocess

from flask.cli import with_appcontext
from flask import current_app
import click

from lib import register_cmd
# pylint: disable=invalid-name
reg_command = register_cmd()


@reg_command
@click.command('lint', help='Lint python app.')
def lint_command():
    """Runs pylint for your source files"""
    click.echo('linted successfully')


@reg_command
@click.command('autopep', help='Confirm your source code to PEP8.')
def autopep_command():
    """Runs auto-formatting to your source files PEP8"""
    autopep = subprocess.call(
        'python -m autopep8 --in-place -r app/'.split()
    )
    sys.exit(autopep)


def register(app):
    '''Registration of cli command to flask environment'''
    reg_command.init(app)
