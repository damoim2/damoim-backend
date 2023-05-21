from django.conf import settings
import boto3
import os

from django.core.files import File

USER_TYPE = 1  # user
POST_TYPE = 2  # post
GROUP_TYPE = 3  # group


class AWSS3:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.S3_ACCESSKEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESSKEY,
        region_name=settings.S3_REGION,
    )

    def upload_file_s3(self, image, filename: str, bucket_type: int):
        try:
            domain = "https://soldoc-server-dev.s3.ap-northeast-2.amazonaws.com/damoim/"
            bucket = "damoim-s3"
            if bucket_type == 1:
                path = "damoim/user/"
            elif bucket_type == 2:
                path = "damoim/post/"
            elif bucket_type == 3:
                path = "damoim/group"
            content_type = "image/jpeg"
            if isinstance(image, File):
                content_type = image.content_type
            url_generator = os.path.join(path, filename)
            ret = self.s3_client.upload_fileobj(
                image,
                bucket,  # "bucket_name",
                url_generator,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": content_type,
                    "ContentDisposition": "attachment; filename*=UTF-8''" + filename,
                },
            )
            return os.path.join(domain, url_generator)
        except Exception as e:
            return e
