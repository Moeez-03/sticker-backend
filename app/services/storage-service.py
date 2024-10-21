import boto3
import digitalocean
from app.core.config import settings

def upload_to_aws_s3(file_data, filename):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3.put_object(Bucket=settings.AWS_BUCKET_NAME, Key=filename, Body=file_data)
    return f"https://{settings.AWS_BUCKET_NAME}.s3.amazonaws.com/{filename}"

def upload_to_do_spaces(file_data, filename):
    client = digitalocean.Spaces(access_key_id=settings.DO_SPACES_KEY,
                                 secret_access_key=settings.DO_SPACES_SECRET)
    client.upload_file(settings.DO_BUCKET_NAME, filename, file_data)
    return f"https://{settings.DO_BUCKET_NAME}.nyc3.digitaloceanspaces.com/{filename}"
