import boto3
from core_api.models.expenses import ExpensesReq


def put_to_expenses(expensesReq: ExpensesReq) -> bool:
    """Mapper to input expenses to AWS

    Returns:
        bool: status
    """
    dynamodb = boto3.resource("dynamodb")
    dynamoTable = dynamodb.Table("Expenses")
    item = {
        "spent_to": expensesReq.spend_to,
        "account": expensesReq.account,
        "expense_type": expensesReq.expense_type,
        "expense_amount": expensesReq.expense_amt,
        "description": expensesReq.description,
        "is_monthly_expense": expensesReq.is_monthlyexpese,
        "is_consumer_bill": expensesReq.is_consumerbill,
        "Expenses": expensesReq.id,
    }
    status = dynamoTable.put_item(Item=item)
    return status
