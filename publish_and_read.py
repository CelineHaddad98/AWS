import subscribe_sqs_to_sns as subscribe


publish = subscribe.SNS.client.publish(
    TopicArn=subscribe.SNS.response['TopicArn'],
    Message='Test Published Message'
)


message = subscribe.SQS.client.receive_message(
    QueueUrl=subscribe.SQS.url
)

print(message)

print(message['Messages'][0]['Body'])

subscribe.SQS.client.delete_message(
    QueueUrl=subscribe.SQS.url,
    ReceiptHandle=message['Messages'][0]['ReceiptHandle']
)
