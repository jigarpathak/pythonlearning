import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CONNECTION_STR = os.getenv("SERVICE_BUS_CONNECTION_STRING")
QUEUE_NAME = os.getenv("QUEUE_NAME")

def send_message():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        with client.get_queue_sender(QUEUE_NAME) as sender:
            message = ServiceBusMessage("Hello, Azure Service Bus!")
            sender.send_messages(message)
            print("Message sent successfully!")

if __name__ == "__main__":
    send_message()
