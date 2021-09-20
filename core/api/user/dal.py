"""
Data Access Layer
"""
from core.api.user.models import UserModel


def create_user(**user_body_request):
    """
    Add new user to the DB.

    Keyword Arguments:
        email (str): user email address.
        username (str): the username of the user.
        password (str): user's password.

    Returns:
        UserModel: user model object.
    """
    return UserModel(**user_body_request).save()

