from .base import *
from dotenv import load_dotenv

load_dotenv(verbose=True)

DEBUG = False

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DAMOIM_DB_NAME"),
        "USER": os.environ.get("DAMOIM_DB_USER"),
        "PASSWORD": os.environ.get("DAMOIM_DB_PASSWORD"),
        "HOST": os.environ.get("DAMOIM_DB"),
        "PORT": os.environ.get("DAMOIM_DB_PORT"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    },
}
S3_REGION = os.environ.get("S3_REGION_DEV")
S3_ACCESSKEY_ID = os.environ.get("S3_ACCESSKEY_ID_DEV")
S3_SECRET_ACCESSKEY = os.environ.get("S3_SECRET_ACCESSKEY_DEV")
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
