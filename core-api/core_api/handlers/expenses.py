from core_api.services import expenses as expenses_services
from core_api.models.expenses import ExpensesReq


def put_to_expenses_handler(expensesReq: ExpensesReq) -> bool:
    """Handler to put expenses to AWS

    Returns:
        bool: status
    """
    return expenses_services.put_to_expenses_service(expensesReq)


def get_expenses_types() -> dict:
    """Handler to get expenses types

    Returns:
        dict: expense_types
    """
    return expenses_services.get_expenses_types()
