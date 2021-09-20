from flask import Blueprint

user_blueprint = Blueprint("user", __name__)

from core.api.user import views