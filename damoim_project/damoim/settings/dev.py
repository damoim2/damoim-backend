from .base import *
from dotenv import load_dotenv

load_dotenv(verbose=True)

DEBUG = True

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    # General schema metadata. Refer to spec for valid inputs
    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#openapi-object
    "TITLE": "Damoim API Document",
    "DESCRIPTION": "Swagger 환경 테스트를 위한 페이지입니다",
    # Optional: MAY contain "name", "url", "email"
    "CONTACT": {"name": "황혁주", "email": "nugulhie@gmail.com"},
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    "SWAGGER_UI_SETTINGS": {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  <- 여기 들어가면 어떤 옵션들이 더 있는지 알수있습니다.
        "dom_id": "#swagger-ui",  # required(default)
        "layout": "BaseLayout",  # required(default)
        "deepLinking": True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        "persistAuthorization": True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        "displayOperationId": True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        "filter": True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    # Optional: MUST contain "name", MAY contain URL
    "LICENSE": {
        "name": "Damoim",
        "url": "",
    },
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SERVE_INCLUDE_SCHEMA": True,  # OAS3 Meta정보 API를 비노출 처리합니다.
    # https://www.npmjs.com/package/swagger-ui-dist 해당 링크에서 최신버전을 확인후 취향에 따라 version을 수정해서 사용하세요.
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.38.0",  # Swagger UI 버전을 조절할수 있습니다.
}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DAMOIM_DB_NAME"),
        "USER": os.environ.get("DAMOIM_DB_USERNAME"),
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
