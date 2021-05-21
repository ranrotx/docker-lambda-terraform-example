import sys

def handler(event, context):
    print("Howdy! Invoke successful")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'        