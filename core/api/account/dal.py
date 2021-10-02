from core.api.account.models import AccountModel


def create_account(**account_details):
    """
    Create new account at the DB.

    Keyword Arguments:
        number (int): account number.
        amount (float): account amount of money.
        user_id = to which user does the account belong.

    Returns:
        AccountModel: account model object.
    """
    return AccountModel(**account_details).save()
