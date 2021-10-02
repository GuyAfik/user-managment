from flask import Flask
from core.api.user import user_blueprint
from core.common.database import init_db


def create_app():
    """
    Creates a new flask application with customized parameters.

    Returns:
        app: Flask object.
    """
    application = Flask(__name__)

    application.register_blueprint(blueprint=user_blueprint)

    init_db()

    return application


app = create_app()
