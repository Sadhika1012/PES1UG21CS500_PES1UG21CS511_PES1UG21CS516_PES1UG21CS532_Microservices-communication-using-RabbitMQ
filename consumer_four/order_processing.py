import pika #type:ignore

def callback(ch, method, properties, body):
    print(f"Order Processing received: {body.decode()}")

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_queue')
    channel.basic_consume(queue='order_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Order Processing is waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_messages()
