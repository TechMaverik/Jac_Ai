"expenses.py"
from pydantic import BaseModel, Field
from typing import Optional


class ExpensesReq(BaseModel):
    """Expenses base model

    id: str
    account:str Account
    description: str Description
    expense_amt: str Expense amount
    expense_type: str Expense type
    is_consumerbill: str Is consumer bill
    is_monthlyexpese: str Is monthly expense
    spend_to: str Amount spent to
    """

    id: str
    account: Optional[str] = None
    description: Optional[str] = None
    expense_amt: Optional[int] = 0
    expense_type: Optional[str] = None
    is_consumerbill: Optional[bool] = False
    is_monthlyexpese: Optional[bool] = False
    spend_to: Optional[str] = None
