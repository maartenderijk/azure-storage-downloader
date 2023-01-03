# download_blobs.py
# Python program to bulk download blob files from azure storage
# Uses latest python SDK() for Azure blob storage
# Requires python 3.6 or above
import os
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient


class AzureBlobFileDownloader:
  def __init__(self, connection_string, container_name, local_path):
    print("Intializing AzureBlobFileDownloader")

    # Initialize the connection to Azure storage account
    self.blob_service_client =  BlobServiceClient.from_connection_string(connection_string)
    self.my_container = self.blob_service_client.get_container_client(container_name)
    self.path = local_path


  def save_blob(self,file_name,file_content):
    # Get full path to the file
    download_file_path = os.path.join(self.path, file_name)

    # for nested blobs, create local path as well!
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)

    with open(download_file_path, "wb") as file:
      file.write(file_content)

  def download_all_blobs_in_container(self):
    my_blobs = self.my_container.list_blobs()
    for blob in my_blobs:
      print(blob.name)
      bytes = self.my_container.get_blob_client(blob).download_blob().readall()
      self.save_blob(blob.name, bytes)

# Initialize class and upload files
if __name__ == '__main__':
    # IMPORTANT: Replace connection string with your storage account connection string
    # Usually starts with DefaultEndpointsProtocol=https;...
    conn = "DefaultEndpointsProtocol=https;AccountName=dlsfunctionbesafedevtest;AccountKey=gYdsUWqHLkf4fim4IRnr9bKNUQNZd9QGvrbfeYdcxPf13UjCAkQ985c2IvkDMUlXsPPKy0uFuGHlrufq/9gZJg==;EndpointSuffix=core.windows.net"

    # Replace with blob container
    container_name = "azure-webjobs-secrets"

    # Replace with the local folder where you want files to be downloaded
    local_path = "."

    azure_blob_file_downloader = AzureBlobFileDownloader(conn, container_name, local_path)
    azure_blob_file_downloader.download_all_blobs_in_container()