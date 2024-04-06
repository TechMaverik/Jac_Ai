"expenses.py"
from pydantic import BaseModel, Field


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

    account: str = Field(None)
    description: str = Field(None)
    expense_amt: int = Field(0)
    expense_type: str = Field(None)
    is_consumerbill: bool = Field(False)
    is_monthlyexpese: bool = Field(False)
    spend_to: str = Field(None)
    date: str = Field(None)
    user: str
