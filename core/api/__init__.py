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

    # before_request_middleware(app=app)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NetworkSecurityDB.db'

    init_db()

    return application


app = create_app()
