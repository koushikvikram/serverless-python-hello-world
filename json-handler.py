import json


def hello(event, _context):
    message = f"Hello {event['name']}"
    
    response = {
        "statusCode": 200,
        "body": json.dumps(message)
    }
    
    return response