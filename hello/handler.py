import json
import requests
import bcrypt

def hello(event, context):
    name = 'anonymous'
    hashed = bcrypt.hashpw(name, bcrypt.gensalt())
    body = {
        "message": "requests {}, bcrypt {} installed. hash generated: {}".
            format(requests.__version__, bcrypt.__version__, hashed),
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
