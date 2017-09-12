import pika


class MQ:
    def __init__(self):
        pass

    conn = pika.BlockingConnection(pika.URLParameters("amqp://localhost"))
    channel = conn.channel()
    channel.queue_declare(queue='hello')
