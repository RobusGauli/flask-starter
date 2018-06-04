# -*- coding: utf-8 -*-
import click
import subprocess

from lib import register_cmd

_register = register_cmd()


@_register
@click.command('lint', help='Lint python app.')
def lint_command():
    click.echo('linted successfully')


@_register
@click.command('autopep', help='Conform your source code to PEP8.')
def autopep_command():
    autopep = subprocess.call(
        'python -m autopep8 --in-place -r app/'.split()
    )
    if autopep:
        click.echo('Autopep8 is successfully applied.')


def register(app):
    '''Registration of cli command to flask environment'''
    _register.init(app)
