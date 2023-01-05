from azure.storage.blob import BlobServiceClient
from blob_download import AzureBlobFileDownloader
from os import path

connect_str = ""

blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(connect_str)
container_list = blob_service_client.list_containers()

for container in container_list:
    try:
        print(container.name)
        azure_blob_file_downloader = AzureBlobFileDownloader(connect_str, container.name, path.join("export", container.name)) #type: ignore
        azure_blob_file_downloader.download_all_blobs_in_container()

    except Exception as e:
        print(e)


