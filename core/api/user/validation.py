import re

from core.common.exceptions import InvalidPassword


def is_valid_password(password):
    """
    Verifies whether a password is valid or not.

    Primary conditions for password validation:

    * Minimum 8 characters.
    * The alphabets must be between [a-z]
    * At least one alphabet should be of Upper Case [A-Z]
    * At least 1 number or digit between [0-9].
    * At least 1 special character from [ _ or @ or $ or ! or # or & or ^].

    Args:
        password (str): user's password.

    Raises:
        bool: True if password is valid, False if not.
    """
    if len(password) < 8:
        raise InvalidPassword(err_msg="Password must be more than 8 characters or more")
    if re.search(pattern="[a-z]", string=password):
        raise InvalidPassword(err_msg="Password must contain at least one small english character")
    if re.search(pattern="[A-Z]", string=password):
        raise InvalidPassword(err_msg="Password must contain at least one big english character")
    if re.search(pattern="[0-9]", string=password):
        raise InvalidPassword(err_msg="Password must contain at least one number")
    if re.search(pattern="[!@#$%^&*_]", string=password):
        raise InvalidPassword(err_msg="Password must contain at least one special character")
    if re.search(pattern="\s", string=password):
        raise InvalidPassword(err_msg="Password must not contain white spaces")
