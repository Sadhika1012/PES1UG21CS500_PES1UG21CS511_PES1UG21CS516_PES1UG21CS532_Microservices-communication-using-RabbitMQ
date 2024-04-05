import pika #type:ignore

def callback(ch, method, properties, body):
    print(f"Stock Management received: {body.decode()}")

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='stock_queue')
    channel.basic_consume(queue='stock_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Stock Management is waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_messages()
