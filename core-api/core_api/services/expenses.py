import random
from core_api.mappers import expenses as expenses_mappers
from core_api.models.expenses import ExpensesReq
from core_api.configurations import menu_config


def create_id() -> int:
    generated_id = random.randint(1, 999999999999)
    return generated_id


def is_monthly_expense(expense_type: str) -> bool:
    """Is monthly expense

    Returns:
        bool: status
    """
    for item in menu_config.monthly_expense:
        if item == expense_type:
            return True
    else:
        return False


def is_consumer_bill(expense_type: str) -> bool:
    """Is consumer bill

    Returns:
        bool: status
    """
    for item in menu_config.consumer_bill:
        if item == expense_type:
            return True
    else:
        return False


def put_to_expenses_service(expensesReq: ExpensesReq) -> bool:
    """Service to put expenses to AWS

    Returns:
        bool: status
    """
    item = {
        "spent_to": expensesReq.spend_to,
        "account": expensesReq.account,
        "expense_type": expensesReq.expense_type,
        "expense_amount": expensesReq.expense_amt,
        "description": expensesReq.description,
        "is_monthly_expense": is_monthly_expense(expensesReq.expense_type),
        "is_consumer_bill": is_consumer_bill(expensesReq.expense_type),
        "ID": create_id(),
    }
    return expenses_mappers.put_to_expenses_mapper(item)


def get_expenses_types() -> list:
    """Service to get expenses types

    Returns:
        dict: expenses_types
    """

    expenses_types = menu_config.expense_type_menu
    return expenses_types
