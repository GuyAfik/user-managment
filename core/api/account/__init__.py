from flask import Blueprint

account_blueprint = Blueprint("account", __name__)

from core.api.account import views
