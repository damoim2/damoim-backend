from django.utils.deprecation import MiddlewareMixin


class ReponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response_format = {"success": bool, "data": dict}
        error_response_format = {
            "success": False,
            "data": {"code": "0005", "message": "알 수 없는 에러"},
        }

        if (
            hasattr(response, "process_response")
            and getattr(response, "process_response") is not None
        ):
            try:
                data = response.data
                response_format["data"] = data
                response_format["success"] = True
                data = response_format
            except (KeyError, TypeError):
                data = error_response_format
            response.data = data
        else:
            response.data = error_response_format
        return response
