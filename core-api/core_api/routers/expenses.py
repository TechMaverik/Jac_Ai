from fastapi import APIRouter, Request
from core_api.handlers.expenses import put_to_expenses_handler
from core_api.models.expenses import ExpensesReq

prefix = "/expenses"
router = APIRouter(prefix=prefix)


@router.put("/")
def put_to_expenses_routers(expensesReq: ExpensesReq) -> bool:
    """Router to put expenses to AWS

    Returns:
        bool: status
    """
    return put_to_expenses_handler(expensesReq)
