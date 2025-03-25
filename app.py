#Storage account demo
from azure.storage.blob import BlobServiceClient

# Step 1: Connect to Azure Blob Storage
connection_string = "your_connection_string_here"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Step 2: List Storage Account Metadata (Properties)
properties = blob_service_client.get_service_properties()
print(f"Storage Account Properties: {properties}")

# Step 3: List Containers
print("Containers in the Storage Account:")
containers = blob_service_client.list_containers()
for container in containers:
    print(f" - {container['name']}")

# Step 4: List Blob Files from a Specific Container
container_name = "your-container-name"
container_client = blob_service_client.get_container_client(container_name)

print(f"Blobs in '{container_name}':")
blobs = container_client.list_blobs()
for blob in blobs:
    print(f" - {blob.name}")

# Step 5: Create a New Container
new_container_name = "new-container-name"
try:
    blob_service_client.create_container(new_container_name)
    print(f"Container '{new_container_name}' created successfully!")
except Exception as e:
    print(f"Error creating container: {e}")
