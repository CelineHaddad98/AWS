import boto3
from os import getenv
 
 
LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")
 

client = boto3.client("sns", endpoint_url=LOCALSTACK_ENDPOINT_URL)

response = client.create_topic(
    Name='MyTopic'
)
topics = client.list_topics()
print(topics)
