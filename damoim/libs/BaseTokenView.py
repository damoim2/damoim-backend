from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from damoim.libs.ReturnResponse import ReturnResponse
from rest_framework.status import HTTP_200_OK
class BaseTokenObtainView(TokenObtainPairView):
    def __init__(self):
        super().__init__(self)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return ReturnResponse(serializer.validated_data, status=HTTP_200_OK)


