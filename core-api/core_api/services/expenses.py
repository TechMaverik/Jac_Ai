from core_api.mappers.expenses import put_to_expenses_mapper
from core_api.models.expenses import ExpensesReq


def put_to_expenses_service(expensesReq: ExpensesReq) -> bool:
    """Service to put expenses to AWS

    Returns:
        bool: status
    """
    return put_to_expenses_mapper(expensesReq)
