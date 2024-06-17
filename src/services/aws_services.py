# aws_services.py
import boto3
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class S3CSVReader:
    def __init__(self):
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        region_name = os.getenv('AWS_REGION')

        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.s3 = self.session.client('s3')

    def read_csv_from_s3(self, bucket_name, file_name):
        try:
            response = self.s3.get_object(Bucket=bucket_name, Key=file_name)
            status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

            if status == 200:
                print(f"Successful S3 get_object response. Status - {status}")
                csv_content = response['Body'].read().decode('utf-8')
                df = pd.read_csv(StringIO(csv_content))
                return df
            else:
                print(f"Unsuccessful S3 get_object response. Status - {status}")
                return None
        except Exception as e:
            print(f"Error reading CSV from S3: {e}")
            return None

    def get_graph_signed_url(self, bucket_name, file_name, image_buffer):
        self.s3.upload_fileobj(image_buffer, bucket_name, file_name)

        # Generate a signed URL for the uploaded file
        expiration = 3600  # Time in seconds for the URL to remain valid
        signed_url = self.s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': file_name},
                                                    ExpiresIn=expiration)

        return signed_url
