from django.db import transaction
from rest_framework import status

from libs.auth.views import AESCipher
from libs.base.views import BaseModelViewSet
from libs.Logger import Logging
from libs.base.response import ReturnResponse

from libs.auth.Token import Token
from user.models import SocialToUser, KakaoAuth, User, TokenRepository
from user.serializer.UserSerializer import UserCreateSerializer, KakaoAuthSerializer

# 일단 로그인, 토큰 갱신까지 만들고 Users 데이터 베이스로 사용자 프로필 데이터베이스 작성해야함
# Todo 유저 관련 데이터 생각하고 다이어그램 그려서 DB 작성하기
logger = Logging("AUTH")


class Refresh(BaseModelViewSet):
    """
    토큰 갱신 부분
    1. 토큰 기간 검증,
    2. 토큰 갱신
        - 토큰 디코드 후 나오는 refresh 테이블에서 검증, uuid 반환
    3. 토큰 발급
    """

    def post(self, request):
        refresh_token = request.headers.get("Authroization")
        access_token = Token().refresh_access_token(refresh_token)
        return ReturnResponse(
            flag=True, code="SERV0000", data=access_token, status=status.HTTP_200_OK
        )


class SignIn(BaseModelViewSet):
    """
    로그인
    1. 카카오 uuid 혹은, 소셜 로그인 성공 시
    2. 토큰 반환
    """

    def post(self, request):
        kakao_auth = request.headers.get("kakao-access-token")
        if KakaoAuth.objects.filter(kakao_id=kakao_auth).exists():
            user_instance = User.objects.get(socialtouser__social_id=kakao_auth)
            token_library = Token().create_token_pair(user_id=user_instance.user_id)
        return ReturnResponse(
            data=token_library, flag=True, code="SERV0000", status=status.HTTP_200_OK
        )


class SignUp(BaseModelViewSet):
    """
    회원가입 부분
    1. 소셜 uuid 발급,
    2. 받은 uuid와 User 매칭
    3. 정보 저장
    4. 토큰 발급
    """

    def post(self, request):
        with transaction.atomic:
            user_serailizer = UserCreateSerializer(data=request.data)
            if user_serailizer.is_valid:
                data = user_serailizer.create(user_serailizer.validated_data)
            kakao_form = {
                "kakao_id": request.headers.get("kakao-access-token"),
                "name": request.data.get("name"),
            }
            kakao_serializer = KakaoAuthSerializer(kakao_form)
            if kakao_serializer.is_valid:
                kakao_data = kakao_serializer.create(kakao_serializer.validated_data)
            SocialToUser.objects.create(
                user_id=data.user_id, social_id=kakao_data.kakao_id
            )
            token_library = Token().create_token_pair(data.user_id)
        return ReturnResponse(
            data=token_library, flag=True, code="SERV0000", status=status.HTTP_200_OK
        )


class SignOut(BaseModelViewSet):
    def post(self, request):
        token = request.headers.get("Authorization")
        token_instance = TokenRepository.objects.get(token=token)
        token_instance.delete()
        return ReturnResponse(
            flag=True, data=None, code="SERV0000", status=status.HTTP_205_RESET_CONTENT
        )
