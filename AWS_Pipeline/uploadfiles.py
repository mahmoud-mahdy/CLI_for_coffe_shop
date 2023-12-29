import os
import boto3

def upload_files_to_s3(folder_path, bucket_name):
    # s3 = boto3.client('s3')
    session = boto3.Session(profile_name='mahmoud')
    s3 = session.client('s3', region_name='eu-west-1')

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3.upload_file(file_path, bucket_name, file)


    print("Files uploaded successfully!")

# Replace 'folder_path' with the path to your folder in VS Code
folder_path = 'C:\\Users\\ellathy\\Desktop\\data_engineer\\group_project\\team-2-project\\data'

# Replace 'bucket_name' with the name of your S3 bucket
bucket_name = 'de-x5-lle-data-xcelerator-cafe-data'

upload_files_to_s3(folder_path,bucket_name)