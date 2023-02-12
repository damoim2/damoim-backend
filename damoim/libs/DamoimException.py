from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from STATIC_LITERAL_VALUE import ERROR_CODE
class DamoimException(APIException):
    def __init__(self, code: str, flag: bool):
        self.code: str = code
        self.flag: bool = flag
        super().__init__()
    pass

class NotAuthenticated(DamoimException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1001"]
    super().__init__(code="1001", flag=False)
class PermissionDenied(DamoimException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = ERROR_CODE["1002"]
    super().__init__(code="1002", flag=False)
class HTTP404(DamoimException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = ERROR_CODE["1004"]
    super().__init__(code="1004", flag=False)
class ClientValueError(DamoimException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = ERROR_CODE["1003"]
    super().__init__(code="1003", flag=False)

class AuthenticationFailed(DamoimException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1001"]
    super().__init__(code="1001", flag=False)

class InvalidToken(AuthenticationFailed):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = ERROR_CODE["1007"]
