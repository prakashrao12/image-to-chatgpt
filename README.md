# image-to-chatgpt
A user will upload a specific image which has specific question in it, AWS lambda will call Textract to extract text from it and calls chatGPT to get a response to that specific question


Environment variables to be added in lambda:

openai_secret_key_env : api key generated in chatgpt
model_chatgpt         : model name of chatgpt
output_bucket_name    : bucket output name
