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
                "code": self.__class__.code(),
                "message": self.err_msg,
                "type": self.__class__.__name__
            }
        }

    @classmethod
    def code(cls):
        """
        Get status code.

        Returns:
            int: error status code.
        """
        return cls.status_code


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
    Base class for a bad body request.
    """
    status_code = HttpCodes.BAD_REQUEST


class UnAuthorized(BaseApiException):
    """
    Base class for unauthorized operations.
    """
    status_code = HttpCodes.UNAUTHORIZED


class ForbiddenOperation(BaseApiException):
    """
    Base class for forbidden operations.
    """
    status_code = HttpCodes.FORBIDDEN
