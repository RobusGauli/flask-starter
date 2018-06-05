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


@reg_command
@click.command('clean-pyc', help='Remove python artifacts.')
def clean_pyc_command():
    """Removes python artifacts"""
    s = subprocess.call(
        "find . -name '*.pyc' -exec rm -f {} +".split()
    )
    print(s)
    subprocess.call(
        "find . -name '__pycache__' -exec rm -fr {} +".split()
    )
    print('done')


def register(app):
    '''Registration of cli command to flask environment'''
    reg_command.init(app)
