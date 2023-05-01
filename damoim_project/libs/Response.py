from rest_framework.response import Response as baseResponse


class Response(baseResponse):
    def __init__(
        self,
        data=None,
        status=None,
        flag=True,
        code="0000",
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):
        data = {"is_success": flag, "code": code, "data": data}
        super().__init__(
            data=data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
        )
