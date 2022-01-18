import create_queue as SQSclient


response = SQSclient.client.send_message(
    QueueUrl=SQSclient.url,
    MessageBody='Test Message')

message = SQSclient.client.receive_message(
    QueueUrl=SQSclient.url)


print(message)
