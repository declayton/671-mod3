"""
    This program sends a message to a queue on the RabbitMQ server.

    Name: Deanna Clayton
    Date: 1-30-23
    
    Author: Denise Case
    Date: January 14, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LocalHost"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# variable to hold the message
message = "Hi, this is Deanna!"
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body= message)
# print a message to the console for the user
print(' [x] Sent "', message, '"')
# close the connection to the server
conn.close()
