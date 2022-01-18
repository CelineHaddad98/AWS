import boto3
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

client = boto3.client("sqs", endpoint_url=LOCALSTACK_ENDPOINT_URL)

response = client.create_queue(
    QueueName='MyQueue'
)

urldict = client.get_queue_url(QueueName='MyQueue')

url = urldict['QueueUrl']

queue = client.get_queue_attributes(QueueUrl=url)
print(queue)
