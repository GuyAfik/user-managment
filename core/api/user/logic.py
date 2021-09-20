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
