import json
import os
import boto3
import http.client
import urllib.parse

def lambda_handler(event, context):
    # Read OpenAI API credentials from environment variables
    openai_secret_key = os.environ['CREDENTIALS']
    
    # Set up HTTP connection to OpenAI API endpoint
    connection = http.client.HTTPSConnection('api.openai.com')
    
    # Define request parameters
    prompt = 'say my name'
    model = 'text-davinci-002'
    data = {
        'prompt': prompt,
        'model': model,
        'max_tokens': 50
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_secret_key}'
    }
    
    # Send API request and parse response
    connection.request('POST', '/v1/completions', json.dumps(data), headers)
    response = connection.getresponse()
    response_data = json.loads(response.read().decode())
    completion_text = response_data['choices'][0]['text']
    
    # Print generated text
    print(completion_text)
    
    # Return response to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps({'text': completion_text})
    }
