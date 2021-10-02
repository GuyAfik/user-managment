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
