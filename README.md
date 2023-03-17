# image-to-chatgpt

- [image-to-chatgpt](#image-to-chatgpt)
  - [Summary](#summary)
  - [Topology](#topology)
  - [Region](#region)
  - [Environments Variables](#environments-variables)


## Summary
The workflow starts where user uploads images to an AWS S3 bucket, where AWS Lambda is triggered to process the image using Amazon Textract. Textract extracts text from the images with high accuracy and then forwards it to ChatGPT. ChatGPT, being an advanced language model, analyzes the extracted text and generates a thoughtful response based on the provided context.

## Topology

![text](topology.png "AWS to ChatGPT")

## Region

This project has been developed in AWS East-Region to simplify communication among AWS services.

## Environments Variables

Environment variables to be added in lambda:

processed_data_bucket_name  : extracted data bucket name

openai_secret_key_env       : api key generated in chatgpt

model_chatgpt               : model name of chatgpt

output_bucket_name          : bucket output name
