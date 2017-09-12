from MQ import MQ

MQ.channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


MQ.channel.basic_consume(callback,
                         queue='hello',
                         no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
MQ.channel.start_consuming()
