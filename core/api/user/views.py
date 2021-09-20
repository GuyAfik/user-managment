"""
Presentation Layer
"""
from core.api.user import user_blueprint
from core.api.user import logic
from flask import request
from core.common.http_utils import HttpMethods


@user_blueprint.route("/User", methods=[HttpMethods.POST])
def create_user():
    """
    Create user endpoint.

    Returns:
        dict: user model dict representation.
    """
    return logic.create_user(**request.json)
