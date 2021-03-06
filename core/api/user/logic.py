"""
Business logic layer
"""
import hashlib

from core.api.user import dal
from core.common.middleware.response import http_response
from core.common.http_utils import HttpCodes
from core.common.encryptions_utils import hash_
from core.api.user.errors import UnAuthorizedUser, ForbiddenUser


@http_response(code=HttpCodes.OK)
def create_user(**user_body_request):
    """
    Create a new user.

    Keyword Arguments:
        email (str): user email address.
        username (str): the username of the user.
        password (str): user's password.

    Returns:
        dict: user model dict representation.
    """
    _password = "password"

    if _password in user_body_request:
        user_body_request[_password] = hash_(string=user_body_request[_password])
    return dal.create_user(**user_body_request).to_dict()


@http_response(code=HttpCodes.OK)
def get_user(user_id):
    """
    Get an existing user.

    Args:
        user_id (str): the ID of the user.

    Returns:
        dict: user model dict representation.
    """
    return dal.get_user(user_id=user_id).to_dict()


@http_response(code=HttpCodes.OK)
def get_users():
    """
    Get all the users.

    Returns:
        list[dict]: users model dict representation.
    """
    return [user.to_dict() for user in dal.get_users()]


@http_response(code=HttpCodes.NO_CONTENT)
def delete_user(user_id):
    """
    Delete user.

    Args:
        user_id (str): the ID of the user to delete.
    """
    dal.delete_user(user_id=user_id)


@http_response(code=HttpCodes.NO_CONTENT)
def update_user(user_id, **user_body_response):
    """
    Update user properties.

    Args:
        user_id (str): the ID of the user.

    Keyword Arguments:
        email (str): user email address.
        username (str): the username of the user.
        password (str): user's password.
        login_attempts (int): user login attempts.
    """
    dal.update_user(user_id=user_id, **user_body_response)


@http_response(code=HttpCodes.OK)
def login(user_id, username, password):
    """
    Login into a user.

    Args:
        user_id (str): user ID.
        username (str): user name.
        password (str): user password.

    Returns:
        dict: user model dict representation

    Raises:
        UnAuthorizedUser: in case user tried to login with wrong credentials.
        ForbiddenUser: in case user put more than 3 times wrong credentials.
    """
    user = dal.get_user(user_id=user_id)
    if username != user.username or hash_(string=password) != user.password:
        if user.login_attempts > 2:
            raise ForbiddenUser(
                err_msg=f"User {user_id} filled up wrong credentials more than 3 attempts. user is blocked!"
            )
        user.login_attempts += 1
        dal.update_user(user_id=user_id, login_attempts=user.login_attempts)
        raise UnAuthorizedUser(err_msg=f"User {user_id} credentials are not valid")
    return user.to_dict(exclude=["password"])
