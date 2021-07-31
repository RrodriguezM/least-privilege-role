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
    client_s3 = boto3.client('s3')
    list_object_resp = client_s3.list_objects(
        Bucket=bucket_name['Parameter']['Value']
    )
    objects_names = [object['Key'] for object in list_object_resp['Contents']]
    print(objects_names)
    response = client_ssm.get_parameter(Name='/playground/accessanalyzer')
    print(response['Parameter']['Value'])
    print('{{"objects":{}}}'.format(objects_names))
    return {
        'statusCode': 200,
        'body': json.dumps({"objects": objects_names})
    }
