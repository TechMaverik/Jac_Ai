"""expenses.py"""

import boto3
from core_api.models.expenses import ExpensesReq



def put_to_expenses_mapper(item:dict) -> bool:
    """Mapper to put expenses to AWS

    Returns:
        bool: status
    """
    dynamodb = boto3.resource("dynamodb")
    dynamoTable = dynamodb.Table("Expenses")    
    status = dynamoTable.put_item(Item=item)
    if status["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True
    else:
        return False
