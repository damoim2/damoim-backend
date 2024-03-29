"""
Django settings for Damoim project.
Generated by 'django-admin startproject' using Django 3.2.6.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import datetime
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

############## load dot env ##############
load_dotenv(verbose=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Application definition

# "ebhealthcheck.apps.EBHealthCheckConfig",
INSTALLED_APPS = [
    "user",
    "banking",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "libs.base.middleware.ReponseMiddleware",
]
ROOT_URLCONF = "damoim.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "damoim.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# AUTH_USER_MODEL = "Damo.User"


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    # 'REFRESH_TOKEN_LIFETIME': datetime.timedelta(minutes=3),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    # 'AUTH_HEADER_TYPES': ('JWT',),
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
}
"""
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}
"""

AUTH_USER_MODEL = "user.User"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 로그 형식 추가
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # True일경우 이미 존재하는 로거들을 비활성화
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",  # DEBUG가 True일 때 레코드를 전달합니다 뭔소린지
        },
    },
    # 로그텍스트 형식정의
    "formatters": {
        "formatNormal": {"format": "%(levelname)s %(message)s [%(name)s:%(lineno)s]"},
        "formatTime": {
            "format": "[%(asctime)s] %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        # 파일 저장방식
        "info_log": {
            "level": "INFO",  # 설정한 레벨이상의 로그만 동작합니다.
            "class": "logging.handlers.RotatingFileHandler",  # 파일처리 핸들러로 파일저장
            "filename": os.path.join(
                BASE_DIR.parent,
                "logs/info_log_"
                + datetime.datetime.now().strftime("%Y-%m-%d")
                + ".log",
            ),
            "encoding": "UTF-8",  # 인코딩 깨지지 말라고
            "maxBytes": 1024 * 1024 * 5,  # 5 MB  /
            "backupCount": 5,
            "formatter": "formatTime",
        },
        "error_log": {
            "level": "ERROR",  # 설정한 레벨이상의 로그만 동작합니다.
            "class": "logging.handlers.RotatingFileHandler",  # 파일처리 핸들러로 파일저장
            "filename": os.path.join(
                BASE_DIR.parent,
                "logs/error_log_"
                + datetime.datetime.now().strftime("%Y-%m-%d")
                + ".log",
            ),
            "encoding": "UTF-8",  # 인코딩 깨지지 말라고
            "maxBytes": 1024 * 1024 * 5,  # 5 MB  /
            "backupCount": 5,
            "formatter": "formatTime",
        },
        # 콘솔(터미널)에 출력
        "console": {
            "level": "DEBUG",  # 설정한 레벨이상의 로그만 동작합니다.
            "class": "logging.StreamHandler",  # stream으로 로깅출력
            "formatter": "formatTime",
        },
    },
    # 1. 설정한 레벨이상의 로그만 동작합니다.  DEBUG < INFO < WARNING < ERROR < CRITICAL
    # 2. 로깅종류  . 으로 상황별 categorize 가능
    # 3. 로거명은 2개만들면 2개작동하는게 아니라 최하단것만 작동
    "loggers": {
        "django.server": {
            "handlers": ["console", "error_log", "info_log"],
            "propagate": False,
            "level": "DEBUG",  # 설정한 레벨이상의 로그만 동작합니다.
        },
        # 'django.info': {
        #     'handlers': ['console', 'info_log'],
        #     'propagate': True,
        #     'level': 'DEBUG',  # 설정한 레벨이상의 로그만 동작합니다.
        # },
        # 'django.error': {
        #     'handlers': ['console', 'error_log'],
        #     'propagate': False,
        #     'level': 'WARNING',  # 설정한 레벨이상의 로그만 동작합니다.
        # },
    },
}
