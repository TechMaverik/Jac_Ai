"""accounts.py"""

from pydantic import BaseModel, Field


class AccoutDetailReq(BaseModel):
    """Account details request model


    account: str bank account
    balance: int bank balance

    """

    account: str
    balance: str
    user: str
