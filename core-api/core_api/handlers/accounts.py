"""accounts.py"""

from core_api.services import accounts as accounts_services
from core_api.models.accounts import AccoutDetailReq


def put_to_accounts(accountReq: AccoutDetailReq) -> bool:
    """Handlers to put account details to AWS

    Returns:
        bool: status
    """
    return accounts_services.put_to_accounts(accountReq)


def get_account_details() -> list:
    """Handler to get account details

    Returns:
        list: Account details
    """
    return accounts_services.get_account_details()
