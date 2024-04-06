"""accounts.py"""

import random
from core_api.models.accounts import AccoutDetailReq
from core_api.mappers import accounts as accounts_mappers


def create_id() -> int:
    """Create random identifiers

    Returns:
        int: Generated identifier
    """
    generated_id = random.randint(1, 999999999999)
    return generated_id


def put_to_accounts(accountReq: AccoutDetailReq) -> bool:
    """Services to put account details to AWS

    Returns:
        bool: status
    """
    account_details = {
        "ID": create_id(),
        "account": accountReq.account,
        "balance": accountReq.balance,
        "user": accountReq.user,
    }
    return accounts_mappers.put_to_accounts(account_details)


def get_account_details() -> list:
    """Service to get account details

    Returns:
        list: Account details
    """
    return accounts_mappers.get_account_details()
