import json
import subprocess32

def world(event, context):
    out = subprocess32.check_output(['openssl', 'version']).decode('utf-8')
    body = {
        "message": "subprocess32 checks openssl version {} installed.".format(out),
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
