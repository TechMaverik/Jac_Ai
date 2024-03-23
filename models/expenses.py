"""expenses.py"""

from pydantic import BaseModel
from typing import Optional


class ExpensesReq(BaseModel):
    """Expense request model

    Args:
        spent_to (str): To account
        source (str): From account
        expense_type(str): Expense type
        expense_amount(float): Expense amount
        description(str): Expense description
        is_monthly_expense: Is monthly expense status
        is_consumer_bill: Is consumer bill status
        Expenses:key
    """

    spent_to: str
    account: str
    expense_type: str
    expense_amount: float
    description: str
    is_monthly_expense: bool
    is_consumer_bill: bool
    key: str
