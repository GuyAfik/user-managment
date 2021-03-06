from sqlalchemy.orm.exc import NoResultFound

from core.api.account.models import AccountModel
from core.api.account.errors import AccountNotFound


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


def get_account(account_id):
    """
    Get account from the DB.

    Args:
        account_id (str): account ID.

    Returns:
        AccountModel: account model object.
    """
    try:
        return AccountModel.query.filter(AccountModel.id == account_id).one()
    except NoResultFound:
        raise AccountNotFound(f"Account with ID {account_id} was not found")


def get_accounts():
    """
    Get all the accounts from the DB.

    Returns:
        list[AccountModel]: account model objects.
    """
    return AccountModel.query.all()


def update_account(account_id, **account_details):
    """
    Update account and insert the update to DB.

    Args:
        account_id (str): account ID.

    Keyword Arguments:
        number (int): account number.
        amount (float): account amount of money.
        user_id = to which user does the account belong.

    Returns:
        AccountModel: updated account model object.
    """
    account = get_account(account_id=account_id)
    account.update(**account_details)
    return account
