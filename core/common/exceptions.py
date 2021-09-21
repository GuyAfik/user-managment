from core.common.http_utils import HttpCodes


class BaseApiException(Exception):
    """
    Base exception class.
    """
    status_code = None

    def __init__(self, err_msg):
        self.err_msg = err_msg
        super().__init__(err_msg)

    def __str__(self):
        """
        String representation of the exception.
        """
        return f"Message: {self.err_msg}, error code: {self.status_code}"

    def to_dict(self):
        """
        Dict representation of the object.

        Returns:
            dict: exception as a dict.
        """
        return {
            "error": {
                "code": self.status_code,
                "message": self.err_msg,
                "type": self.__class__.__name__
            }
        }


class ResourceNotFound(BaseApiException):
    """
    Base class for resource that was not found.
    """
    status_code = HttpCodes.NOT_FOUND


class Duplicate(BaseApiException):
    """
    Base class for resource that already exists.
    """
    status_code = HttpCodes.DUPLICATE


class BadRequest(BaseApiException):
    """
    Base class for a bad request body.
    """
    status_code = HttpCodes.BAD_REQUEST


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
