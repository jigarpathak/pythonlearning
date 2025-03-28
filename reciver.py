import os
from azure.servicebus import ServiceBusClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CONNECTION_STR = os.getenv("SERVICE_BUS_CONNECTION_STRING")
QUEUE_NAME = os.getenv("QUEUE_NAME")

def receive_message():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        with client.get_queue_receiver(QUEUE_NAME) as receiver:
            for message in receiver:
                print(f"Received Message: {message.body}")
                receiver.complete_message(message)

if __name__ == "__main__":
    receive_message()
