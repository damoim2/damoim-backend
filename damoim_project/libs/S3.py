import os.path

import boto3  # s3에 이미지를 업로드 할 때 필요
from django.conf import settings
from django.core.files.base import File


# save util
# save s3 multipart file to jpeg ret url
class awsS3boto3:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.S3_ACCESSKEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESSKEY,
        region_name=settings.S3_REGION,
    )
    s3_resource = boto3.resource(
        "s3",
        aws_access_key_id=settings.S3_ACCESSKEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESSKEY,
        region_name=settings.S3_REGION,
    )

    def uploads3(self, image, filename, path, bucket_type=""):
        try:
            domain = settings.S3_DOMAIN
            bucket = settings.S3_BUCKET_PRESCRIPTION
            if bucket_type == "request":
                domain = settings.S3_DOMAIN_REQEUST
                bucket = settings.S3_BUCKET_REQEUST
            content_type = "image/jpeg"
            if isinstance(image, File):
                content_type = image.content_type
            url_generator = os.path.join(path, filename)
            ret = self.s3_client.upload_fileobj(
                image,
                bucket,  # "bucket_name",
                url_generator,
                # [7]
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": content_type,
                    "ContentDisposition": "attachment; filename*=UTF-8''" + filename,
                },
            )

            image_url = os.path.join(domain, url_generator)

            return image_url
        except Exception as e:
            return e

    def upload_file_s3(self, file, filename, path, bucket_type=""):
        try:
            domain = settings.S3_DOMAIN
            bucket = settings.S3_BUCKET_PRESCRIPTION
            if bucket_type == "post":
                domain = settings.S3_DOMAIN_POST
                bucket = settings.S3_BUCKET_POST

            url_generator = os.path.join(path, filename)

            ret = self.s3_client.upload_fileobj(
                file,
                bucket,  # "bucket_name",
                url_generator,
                # [7]
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=euc-kr",
                    "ContentDisposition": "attachment; filename*=UTF-8''" + filename,
                },
            )

            return os.path.join(domain, url_generator)
        except Exception as e:
            return e
