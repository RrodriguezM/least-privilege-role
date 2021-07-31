import json
import boto3

# import requests


def lambda_handler(event, context):
    """This Function reads the files available in a bucket and return the files names

    Args:
        event (ApiGateway Invoke): Event comming from the APIGateway 
        context ([type]): Context Information 

    Returns:
        Json: List of Files availables in the bucket
    """
    client_ssm = boto3.client('ssm')
    bucket_name = client_ssm.get_parameter(Name='/least_privilege/bucket_name')
    return {
        'statusCode': 200,
        'body': json.dumps({"bucketname": bucket_name['Parameter']['Value']})
    }
