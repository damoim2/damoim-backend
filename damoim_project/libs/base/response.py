from rest_framework.response import Response


# Response 반환 폼을 통일시키기 위해서 Custom Response 설정
class ReturnResponse(Response):
    def __init__(self, code: str, flag: bool, data: dict):
        data_dict = {"is_success": flag, "code": code, "data": data}
        super().__init__(data=data_dict)
