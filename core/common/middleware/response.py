from flask import make_response, jsonify
from core.common.exceptions import BaseApiException
from core.common.http_utils import HttpCodes


def http_response(code):
    """
    Decorator to execute all the API services implementations and parse a valid response to them.

    Args:
        code (int): http code that should indicate about success.

    Returns:
        Response: flask api response.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            def _http_response(response, http_status_code):
                """
                Returns an API response for the client.

                Args:
                    response (list/dict/serializable object): api response for the client.
                    http_status_code (int): the http status code that the server should return.

                Returns:
                    Response: a flask response object.
                """
                return make_response(jsonify(response), http_status_code)
            try:
                response = func(*args, **kwargs)
                return _http_response(
                    response=response if code != HttpCodes.NO_CONTENT else "", http_status_code=code
                )
            except BaseApiException as exc:
                return _http_response(response=exc.to_dict(), http_status_code=exc.status_code)
        return wrapper
    return decorator

