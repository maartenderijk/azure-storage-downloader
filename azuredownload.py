from azure.storage.blob import BlobServiceClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=dlsfunctionbesafedevtest;AccountKey=gYdsUWqHLkf4fim4IRnr9bKNUQNZd9QGvrbfeYdcxPf13UjCAkQ985c2IvkDMUlXsPPKy0uFuGHlrufq/9gZJg==;EndpointSuffix=core.windows.net"

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_list = blob_service_client.list_containers()

    for container in container_list:
        container_client = blob_service_client.get_container_client(container.name)
        print(container.name)


except Exception as ex:
    print('Exception:')
    print(ex)