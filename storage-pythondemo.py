from azure.storage.blob import BlobServiceClient

# change your connection string
connection_string = "Your storagea account conn string"

#Create blob service client calss mapping with conn string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
print("Connection established with storage account!!")

#view the storage account peroperties
properties = blob_service_client.get_service_properties()
print(f"Storage account prop: {properties}")

#view the container details
containers = blob_service_client.list_containers()
print("List of containers")
for container in containers:
    print(f"- {container['name']}")

#list blobs from container
container_name = "images"

#Get container client
container_client = blob_service_client.get_container_client(container_name)

#List blobs from the container
print(f"Blobs is '{container_name}':")
blobs = container_client.list_blobs()
for blob in blobs:
    print(f"- {blob.name}")

#Create container using code
new_container_name = "myimages"

try:
    blob_service_client.create_container(new_container_name)
    print(f"Container '{new_container_name}' created successfully!!")
except Exception as e:
    print(f"Error in creating container: {e}")
