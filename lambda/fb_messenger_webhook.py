import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(context)
    
    VERIFY_TOKEN = "ABCD"
    http_method = event.get("requestContext", {}).get("http", {}).get("method")
    
    if http_method == "GET":
       query_params = event.get("queryStringParameters", {})
       verify_token = query_params.get("hub.verify_token")
       challenge = query_params.get("hub.challenge")
       
       if verify_token != VERIFY_TOKEN:
          return {"statusCode": 403, "body": "Forbidden"}
       return {"statusCode": 200, "body": challenge}
       
    elif http_method == "POST":
       body = json.loads(event.get("body", "{}"))
       return {"statusCode": 200, "body": json.dumps({"status": "success"})}
    else:
       return {"statusCode": 405, "body": "Method Not Allowed"}
