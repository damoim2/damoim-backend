from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import tokens
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer


class RefreshView(jwt_views.TokenRefreshView):
    # permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(jwt_views.TokenObtainPairView):
    permission_classes = [
        permissions.AllowAny,
    ]
    user_serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)

            if response.status_code == status.HTTP_200_OK:
                user = get_user_model().objects.get(
                    username=request.data[get_user_model().USERNAME_FIELD]
                )
                # info = UserAddInfos.objects.get(fk_uuid=user.uuids)

                serialized_user = self.user_serializer_class(user)
                response.data.update(serialized_user.data)
                contact_number = None
                # 병원의 경우에만 contact_number가 사용되므로 병원을 제외한 부분에서는 null값을 보냄
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(
            data={
                "username": self.soldoc_admin_id,
                "password": self.soldoc_admin_pw,
                "uuids": self.uuid,
            }
        )
        return Response(status=status.HTTP_201_CREATED)
