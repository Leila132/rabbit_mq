from log_generator import Logger_generator
import pika
import time
import json


while True:
    time.sleep(5)

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    logger = Logger_generator()
    new_note = logger.generate_log()
    print(new_note)

    if logger.level == "INFO":
        channel.queue_declare(queue="green")
        channel.basic_publish(
            exchange="", routing_key="green", body=json.dumps(new_note)
        )

    else:
        channel.queue_declare(queue="red")
        channel.basic_publish(exchange="", routing_key="red", body=json.dumps(new_note))

    connection.close()
