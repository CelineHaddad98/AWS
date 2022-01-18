import create_topic as SNS
import create_queue as SQS

subscribe = response = SNS.client.subscribe(
    TopicArn=SNS.response['TopicArn'],
    Protocol='sqs',
    Endpoint=SQS.queue['Attributes']['QueueArn']
)

print(subscribe)
