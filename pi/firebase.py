from google.cloud import storage
import os
os_vid = os.listdir("vid")
# print(os_vid[0])
# Initialize Google Cloud Storage client
client = storage.Client.from_service_account_json('key.json')  # Replace with the path to your key file
bucket_name = 'ad-vid.appspot.com'  # Replace with the name of your Firebase Storage bucket
while True :
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()

# Print the names of all the files

    for blob in blobs:
        if not blob.name in os_vid:
            print(blob.name)
            blob = bucket.blob(blob.name)
            # Specify the local path where you want to save the downloaded video
            local_path = "vid/" + blob.name

            # Download the video file
            blob.download_to_filename(local_path)
    
            print(f"Video downloaded successfully to: {local_path}")
        else:
            print("all set")
