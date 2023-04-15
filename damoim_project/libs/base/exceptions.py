from rest_framework.exceptions import APIException
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from libs.STATIC_LITERAL_VALUE import ERROR_CODE


class DamoimException(APIException):
    code: str
    flag: bool
    pass

class ClientError(DamoimException):
    code = "1"
    flag = False
    status_code = HTTP_400_BAD_REQUEST
    pass
class ServerError(DamoimException):
    code = "0"
    flag = False
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    pass

class ThridPartyError(DamoimException):
    code = "2"
    flag = False
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    pass

class NotAuthenticated(DamoimException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1001"]
    code = "1001"
    flag = False


class PermissionDenied(DamoimException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = ERROR_CODE["1002"]
    code = "1002"
    flag = False


class HTTP404(DamoimException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = ERROR_CODE["1004"]
    code = "1004"
    flag = False


class ClientValueError(DamoimException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = ERROR_CODE["1003"]
    code = "1003"
    flag = False


class AuthenticationFailed(DamoimException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1001"]
    code = "1001"
    flag = False


class InvalidToken(AuthenticationFailed):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1007"]
    code = "1001"
    flag = False


class UnknownError(DamoimException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = ERROR_CODE["1005"]
    code = "1005"
    flag = False
