from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.views import set_rollback
from damoim_project.libs.base.response import ReturnResponse
from damoim_project.libs.base.exceptions import HTTP404, PermissionDenied


def exception_handler(exc, context):
    if isinstance(exc, HTTP404):
        exc = HTTP404()
    elif isinstance(exc, PermissionDenied):
        exc = PermissionDenied()

    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = exc.detail

        set_rollback()
        return ReturnResponse(
            flag=exc.flag,
            code=exc.code,
            data=data,
            status=exc.status_code,
            headers=headers,
        )

    return None
