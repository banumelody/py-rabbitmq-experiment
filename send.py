from MQ import MQ

MQ.channel.basic_publish(exchange='',
                         routing_key='hello',
                         body='Hello World!')

print(" [x] Sent 'Hello World!'")

MQ.conn.close()
