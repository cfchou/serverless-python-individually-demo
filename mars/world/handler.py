import json
import requests
import sys

def world(event, context):
    name = 'anonymous'
    body = {
        "message": "{}, requests {} installed.".
            format(sys.version, requests.__version__),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
