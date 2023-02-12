import boto3
from botocore.exceptions import ClientError

from config.config import Config
from infrastructure.logging import Logger

import os


class S3Storage:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        self.config = Config()
        self.logger = Logger(__name__)
        self.s3 = boto3.client('s3',
                               aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key)
        self.bucket_name = bucket_name

    def create_bucket(self):
        try:
            self.s3.create_bucket(Bucket=self.bucket_name,
                                  CreateBucketConfiguration={
                                    'LocationConstraint': 'us-west-1'
                                  })
        except ClientError as e:
            self.logger.debug(e)

    def upload_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
        except ClientError as e:
            self.logger.debug(e)
            return False
        return True

    def upload_fileobj(self, file_obj, object_name):
        try:
            self.s3.upload_fileobj(file_obj, self.bucket_name, object_name)
        except ClientError as e:
            self.logger.debug(e)
            return False
        return True

    def download_file(self, key, file_path):
        self.s3.download_file(self.bucket_name, key, file_path)

    def get_file(self, key):
        obj = self.s3.Object(self.bucket_name, key)
        file_content = obj.get()['Body'].read().decode('utf-8')
        return file_content

    def update_file(self, key, file_content):
        self.delete_file(key)
        self.upload_file(file_content, key)

    def delete_file(self, key):
        self.s3.Object(self.bucket_name, key).delete()

    def list_files(self):
        return [obj.key for obj in self.s3.Bucket(self.bucket_name)
                .objects.all()]
