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
