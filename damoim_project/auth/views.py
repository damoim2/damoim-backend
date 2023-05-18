from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import tokens
from rest_framework.response import Response
from rest_framework import status, permissions

from libs.swagger.schema.auth import (
    sign_up_swagger,
    sign_in_swagger,
    refresh_swagger,
    sign_out_swagger,
)
from .deserializer import CreateUserDeserializer
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from dataclasses import asdict
from .serializers import CreateUserSerializer


class RefreshView(jwt_views.TokenRefreshView):
    permission_classes = [
        permissions.AllowAny,
    ]

    @extend_schema(**refresh_swagger)
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

    @extend_schema(**sign_in_swagger)
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)

            if response.status_code == status.HTTP_200_OK:
                user = get_user_model().objects.get(
                    username=request.data[get_user_model().USERNAME_FIELD]
                )
                serialized_user = self.user_serializer_class(user)
                response.data.update(serialized_user.data)
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    @extend_schema(**sign_out_swagger)
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = CreateUserSerializer

    @extend_schema(**sign_up_swagger)
    def create(self, request, *args, **kwargs):
        deserializer = CreateUserDeserializer(data=request.data)
        command = deserializer.create()
        serializer = CreateUserSerializer(asdict(command))
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
