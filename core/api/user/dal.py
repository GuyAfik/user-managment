"""
Data Access Layer
"""
from core.api.user.models import UserModel
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from core.common.exceptions import UserNotFound, DuplicateUserEmail


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
    try:
        return UserModel(**user_body_request).save()
    except IntegrityError:
        email = user_body_request.get("email")
        raise DuplicateUserEmail(f"User with email {email} already exists")


def get_user(user_id):
    """
    Get an existing user from the DB.

    Args:
        user_id (str): the ID of the user.

    Returns:
        UserModel: user model object.
    """
    try:
        return UserModel.query.filter(UserModel.id == user_id).one()
    except NoResultFound:
        raise UserNotFound(f"User with ID {user_id} was not found")

