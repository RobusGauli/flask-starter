"""
    Flask SQL session manager
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Provides a local proxy similar to flask.request or flask.current_app
    as flask_sql_session.dbsession

    It creates a unique session for each request scope.
"""

from werkzeug.local import LocalProxy
from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack, current_app

__all__ = ['dbsession', 'FlaskSqlSession']


def _get_session():
    # pylint: disable=missing-docstring, protected-access
    context = _app_ctx_stack.top
    if context is None:
        raise RuntimeError(
            "Could not access db session outside of application context"
        )
    app = current_app._get_current_object()
    if not hasattr(app, 'scopped_session'):
        raise AttributeError(
            "{} has no scoped session attribute."
            "You need to initialize with FlaskSqlSession".format(app)
        )
    return app.scopped_session


# Provides the current sqlalchemy session within the request
dbsession = LocalProxy(_get_session)


class FlaskSqlSession(scoped_session):
    """A class whose scope is set to flask application context"""

    def __init__(self, session_factory, app=None):
        """
        :param session_factory: A callabe that returns a
            :class: `~sqlalchemy.orm.session.Session`
        :param app: a :class: `~flask.Flask` application
        """

        super(FlaskSqlSession, self).__init__(
            session_factory,
            scopefunc=_app_ctx_stack.__ident_func__
        )
        if app is not None:
            self._create_teardown_context(app)

    def _create_teardown_context(self, app):
        app.scopped_session = self

        @app.teardown_appcontext
        def remove_scoped_session(*args, **kwargs):
            # pylint: disable=missing-docstring,unused-argument,unused-variable
            app.scopped_session.remove()
