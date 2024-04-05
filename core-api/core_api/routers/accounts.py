"""accounts.py"""

from fastapi import APIRouter, Request
from core_api.handlers import accounts as accounts_handlers
from core_api.models.accounts import AccoutDetailReq


prefix = "/accounts"
router = APIRouter(prefix=prefix)


@router.put("/add")
def put_to_accounts(accountDetailsReq: AccoutDetailReq) -> bool:
    """Router to put account details to AWS

    Returns:
        bool: status
    """
    return accounts_handlers.put_to_accounts(accountDetailsReq)


@router.get("/all")
def get_account_details() -> list:
    """Router to get account details

    Returns:
        list: Account details
    """
    return accounts_handlers.get_account_details()
