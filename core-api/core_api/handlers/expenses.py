from core_api.services.expenses import put_to_expenses_service
from core_api.models.expenses import ExpensesReq


def put_to_expenses_handler(expensesReq: ExpensesReq) -> bool:
    """Handler to put expenses to AWS

    Returns:
        bool: status
    """
    return put_to_expenses_service(expensesReq)
