from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from libs.base.exceptions import ClientError


class PostCreateError(ClientError):
    status_code = HTTP_400_BAD_REQUEST
    code = "0001"
    default_detail = "글 생성에 실패하였습니다."

class PostGetError(ClientError):
    status_code = HTTP_400_BAD_REQUEST
    code = "0001"
    default_detail = "글 생성에 실패하였습니다."