def lambda_handler(event, context):
    response_body = "<h1> Leaves, leaves, leaves! </h1> <h2> We're insane about leaves </h2> <img src='https://i.imgur.com/O1vWos3.jpg' alt='My leaf' />"
    
    
    return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
    }
}

