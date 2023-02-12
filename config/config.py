from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    # nba api
    API_KEY = os.getenv("NBA_API_KEY")
    API_HOST = os.getenv("NBA_API_HOST")

    # amazon s3 bucket
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME = os.getenv('MS3DM_BUCKET_NAME')
