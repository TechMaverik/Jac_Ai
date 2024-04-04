"""accounts.py"""

import boto3


def put_to_accounts(item: dict) -> bool:
    """Mapper to put account details to AWS

    Returns:
        bool: status
    """
    dynamodb = boto3.resource("dynamodb")
    dynamoTable = dynamodb.Table("Accounts")
    status = dynamoTable.put_item(Item=item)
    if status["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True
    else:
        return False


def get_account_details() -> list:
    """Mapper to return the account details from AWS

    Returns:
        list: Account list
    """
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Accounts")
    response = table.scan()
    accounts = response["Items"]
    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        accounts.extend(response["Items"])
    return accounts
