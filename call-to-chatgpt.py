import os
import json
import boto3
import http.client
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the uploaded file's bucket and key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read the text file from S3
    file_content = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')

    # Store the file content in a Python JSON
    file_json = {'text': file_content}

    # Read OpenAI API credentials from environment variables
    openai_secret_key = os.environ['openai_secret_key_env']
    
    # Set up HTTP connection to OpenAI API endpoint
    connection = http.client.HTTPSConnection('api.openai.com')
    
    # Define request parameters
    prompt = file_json['text']
    model = os.environ['model_chatgpt']
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
    #print(completion_text)
    
    # Define the output bucket and output key (file name)
    output_bucket = os.environ['output_bucket_name']
    output_key = f"{os.path.splitext(os.path.basename(key))[0]}_chatgpt_result.txt"

    # Upload the generated text to the output S3 bucket
    s3.put_object(Bucket=output_bucket, Key=output_key, Body=completion_text)
    
    # Return response to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps({'text': completion_text})
    }
