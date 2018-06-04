# -*- coding: utf-8 -*-
import click

@click.command('lint', help='Lint python app.')
def lint_command():
    click.echo('linted successfully')

def register(app):
    '''Registration of cli command to flask environment'''
    app.cli.add_command(lint_command)
