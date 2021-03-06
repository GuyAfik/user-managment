"""
Presentation Layer
"""
from core.api.user import user_blueprint
from core.api.user import logic
from flask import request
from core.common.http_utils import HttpMethods


@user_blueprint.route("/user", methods=[HttpMethods.POST])
def create_user():
    """
    Create user endpoint.

    Returns:
        dict: user model dict representation.
    """
    return logic.create_user(**request.json)


@user_blueprint.route("/user/<user_id>", methods=[HttpMethods.GET])
def get_user(user_id):
    """
    Get user endpoint.

    Args:
        user_id (str): the ID of the user.

    Returns:
        dict: user model dict representation.
    """
    return logic.get_user(user_id=user_id)


@user_blueprint.route("/users", methods=[HttpMethods.GET])
def get_users():
    """
    Get users endpoint.

    Returns:
        list[dict]: users model dict representation.
    """
    return logic.get_users()


@user_blueprint.route("/user/<user_id>", methods=[HttpMethods.DELETE])
def delete_user(user_id):
    """
    Delete user endpoint.

    Args:
        user_id (str): the ID of the user to delete.

    Returns:
        str: empty response in case of success.
    """
    return logic.delete_user(user_id=user_id)


@user_blueprint.route("/user/<user_id>", methods=[HttpMethods.PUT])
def update_user(user_id):
    """
    Update user endpoint.

    Args:
        user_id (str): the ID of the user to delete.

    Returns:
        str: empty response in case of success.
    """
    return logic.update_user(user_id=user_id, **request.json)


@user_blueprint.route("/login/<user_id>/<username>/<password>", methods=[HttpMethods.GET])
def login(user_id, username, password):
    """
    Login into a user endpoint.

    Args:
        user_id (str): user ID.
        username (str): user name.
        password (str): user password.

    Returns:
        dict: user model dict representation
    """
    return logic.login(user_id=user_id, username=username, password=password)
