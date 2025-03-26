import os
import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient

# Key Vault Details
KEY_VAULT_NAME = "myKeyVault"
SECRET_NAME = "StorageConnectionString"
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"

def get_storage_connection_string():
    """Retrieve Storage Account connection string from Azure Key Vault"""
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=KV_URI, credential=credential)
    retrieved_secret = secret_client.get_secret(SECRET_NAME)
    return retrieved_secret.value

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Azure Function triggered")

    try:
        # Retrieve Storage Account connection string securely
        connection_string = get_storage_connection_string()

        # Connect to Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # List blobs in a container
        container_name = "my-container"
        container_client = blob_service_client.get_container_client(container_name)
        blobs = [blob.name for blob in container_client.list_blobs()]

        return func.HttpResponse(f"Blobs in container '{container_name}': {blobs}", status_code=200)
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
