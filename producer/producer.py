import pika # type: ignore

def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='item_queue')
    channel.basic_publish(exchange='', routing_key='item_queue', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()

if __name__ == '__main__':
    send_message('New item created')  # Example message
