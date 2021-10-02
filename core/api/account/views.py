from flask import request

from core.api.account import account_blueprint
from core.common.http_utils import HttpMethods
from core.api.account import logic


@account_blueprint.route("/account", methods=[HttpMethods.POST])
def create_account():
    """
    Create account endpoint.

    Returns:
        dict: account model dict representation.
    """
    return logic.create_account(**request.json)


@account_blueprint.route("/account/<account_id>", methods=[HttpMethods.GET])
def get_account(account_id):
    """
    Get account from the DB.

    Args:
        account_id (str): account ID.

    Returns:
        dict: account model dict representation.
    """
    return logic.get_account(account_id=account_id)