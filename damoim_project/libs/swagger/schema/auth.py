from rest_framework import status

from auth.deserializer import CreateUserDeserializer
from auth.serializers import CreateUserSerializer
from libs.swagger.serializer.refresh_request_serializer import RefreshRequestSerializer
from libs.swagger.serializer.sign_in_request_serializer import SignInRequestSerializer
from libs.swagger.serializer.sign_in_response_serializer import SignInResponseSerializer
from libs.swagger.serializer.sign_out_request_serializer import SignOutRequestSerializer

sign_up_swagger = {
    "tags": ["Auth"],
    "summary": "Sign Up",
    "request": CreateUserDeserializer,
    "responses": {status.HTTP_200_OK: CreateUserSerializer},
}

sign_in_swagger = {
    "tags": ["Auth"],
    "summary": "Sign In",
    "request": SignInRequestSerializer,
    "responses": {status.HTTP_200_OK: SignInResponseSerializer},
}
refresh_swagger = {
    "tags": ["Auth"],
    "summary": "Refresh",
    "request": RefreshRequestSerializer,
    "responses": {status.HTTP_200_OK: SignInResponseSerializer},
}
sign_out_swagger = {
    "tags": ["Auth"],
    "summary": "Sign Out",
    "request": SignOutRequestSerializer,
    "responses": {status.HTTP_205_RESET_CONTENT: None},
}
