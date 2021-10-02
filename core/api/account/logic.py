from core.api.account import dal
from core.common.middleware.response import http_response
from core.common.http_utils import HttpCodes


@http_response(code=HttpCodes.OK)
def create_account(**account_details):
    """
    Create new account.

    Keyword Arguments:
        number (int): account number.
        amount (float): account amount of money.
        user_id = to which user does the account belong.

    Returns:
        dict: account dict representation
    """
    return dal.create_account(**account_details).to_dict()


def get_account(account_id):
    """
    Get account from the DB.

    Args:
        account_id (str): account ID.

    Returns:
        dict: account model dict representation.
    """
    return dal.get_account(account_id=account_id).to_dict()


def get_accounts():
    """
    Get all the accounts.

    Returns:
        list[dict]: account models dict representation.
    """
    return [account.to_dict() for account in dal.get_accounts()]
