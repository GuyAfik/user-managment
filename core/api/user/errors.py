from core.common.exceptions import ForbiddenOperation, BadRequest, Duplicate, UnAuthorized, ResourceNotFound


class UserNotFound(ResourceNotFound):
    """
    Raised when a user was not found.
    """
    pass


class DuplicateUserEmail(Duplicate):
    """
    Raised when the user email already exists.
    """
    pass


class InvalidPassword(BadRequest):
    """
    Raised when the client provided invalid password requirements.
    """
    pass


class UnAuthorizedUser(UnAuthorized):
    """
    Raised when a user filled up invalid credentials to login.
    """
    pass


class ForbiddenUser(ForbiddenOperation):
    """
    Raised when user tried to login more than 3 times and failed.
    """
    pass
