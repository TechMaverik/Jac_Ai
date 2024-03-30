from fastapi import APIRouter, Request
from core_api.handlers import expenses as expense_handlers
from core_api.models.expenses import ExpensesReq

prefix = "/expenses"
router = APIRouter(prefix=prefix)


@router.put("/")
def put_to_expenses_routers(expensesReq: ExpensesReq) -> bool:
    """Router to put expenses to AWS

    Returns:
        bool: status
    """
    return expense_handlers.put_to_expenses_handler(expensesReq)


@router.get("/types")
def get_expenses_types() -> list:
    """Router to return expense types

    Returns:
        list: expense_types
    """
    return expense_handlers.get_expenses_types()
