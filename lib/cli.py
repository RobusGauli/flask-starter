"""
    lib.cli
    ~~~~~~~~~~
    Helper function that registers command function
    and provides chained function to register commands
    to flask app instance
"""
from functools import wraps


def register_cmd():
    """
        Registration function that returns decorator function for registration
    """
    commands = []

    def deco(func):
        """Decorator function that simply registers func to commands list"""
        commands.append(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def init(app):
        """Helper function that registers commands to flask app"""
        for func in commands:
            app.cli.add_command(func)
    deco.init = init
    return deco


__all__ = ['register_cmd']
