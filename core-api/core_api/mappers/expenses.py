"""expenses.py"""

import boto3


def put_to_expenses(item: dict) -> bool:
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


def get_expenses() -> list:
    """Mapper to return the expenses values from AWS

    Returns:
        list: Expenses
    """
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Expenses")
    response = table.scan()
    expenses = response["Items"]
    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        expenses.extend(response["Items"])
    return expenses
