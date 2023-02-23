from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

from damoim_project.libs.base.views import BaseModelViewSet, BaseTokenObtainView
from damoim_project.libs.Logger import Logging
from damoim_project.user.domain.model.serializer import UserSerializer, CreateUserSerializer
from damoim_project.libs.base.response import ReturnResponse
from damoim_project.libs.base.exceptions import NotAuthenticated, ClientValueError, AuthenticationFailed, UnknownError

#일단 로그인, 토큰 갱신까지 만들고 Users 데이터 베이스로 사용자 프로필 데이터베이스 작성해야함
# Todo 유저 관련 데이터 생각하고 다이어그램 그려서 DB 작성하기
logger = Logging("AUTH")

class Login(BaseTokenObtainView):
    permission_classes = [
        AllowAny,
    ]
    user_serializer_class = UserSerializer
    def __init__(self):
        super().__init__()
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            if response.status_code == status.HTTP_200_OK:
                user = get_user_model().objects.get(
                    username=request.data[get_user_model().USERNAME_FIELD]
                )
                serialized_user = self.user_serializer_class(user)
                response.data.update(serialized_user.data)
            else:
                raise AuthenticationFailed
            return response
        except Exception as e:
            raise ClientValueError
class Register(BaseModelViewSet):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
        except Exception as e:
            raise ClientValueError
        serializer = CreateUserSerializer(
            data={
                "username": username,
                "password": password,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return ReturnResponse(code="0000", flag=True, data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ClientValueError



class LogoutView(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return ReturnResponse(code="0000",flag=True,status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            raise UnknownError

class RefreshAPI(BaseTokenObtainView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except Exception as e:
            return NotAuthenticated

