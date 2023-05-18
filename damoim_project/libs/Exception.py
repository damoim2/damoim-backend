from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST


class DamoimException(APIException):
    tag = "BASE"
    code = "0000"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    title = "기타 오류"
    default_detail = "알 수 없는 에러"


class DamoimClientException(DamoimException):
    tag = "BASE"
    code = "1000"
    status_code = HTTP_400_BAD_REQUEST
    title = "입력 오류"
    default_detail = "입력 값에 오류가 있습니다."


class ClientRequestValidationError(DamoimClientException):
    tag = "REQUEST"
    code = "1001"
    status_code = HTTP_400_BAD_REQUEST
    title = "입력 오류"
    default_detail = "잘못된 값을 입력 받았습니다."
