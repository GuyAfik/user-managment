"""
Business logic layer
"""
from core.api.user import dal
from core.common.middleware.response import http_response
from core.common.http_utils import HttpCodes


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
