"expenses.py"
import boto3
from ..mappers.expenses import ExpensesReq


def put_to_expenses(expenseReq: ExpensesReq):
    """mapper to put expenses in dynamo db

    Args:
        expenseReq (ExpensesReq): _description_
    """

    dynamodb = boto3.resource("dynamodb")
    dynamoTable = dynamodb.Table("Expenses")
    item = {
        "spent_to": expenseReq.spent_to,
        "account": expenseReq.account,
        "expense_type": expenseReq.expense_type,
        "expense_amount": expenseReq.expense_amount,
        "description": expenseReq.description,
        "is_monthly_expense": expenseReq.is_monthly_expense,
        "is_consumer_bill": expenseReq.is_consumer_bill,
        "Expenses": expenseReq.key,
    }
    status = dynamoTable.put_item(Item=item)
    if status is True:
        return {"Is_put_to_expenses": True}
    else:
        return {"Is_put_to_expenses": False}
