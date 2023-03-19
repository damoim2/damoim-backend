from libs.base.views import BaseModelViewSet
from libs.Logger import Logging

from libs.base.response import ReturnResponse

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
        return ReturnResponse()

class SignIn(BaseModelViewSet):
    """
    로그인
    1. 아이디, 비밀번호 검증
    2. 토큰 반환
    """
    def post(self, request):
        return ReturnResponse()


class SignUp(BaseModelViewSet):
    """
    회원가입 부분
    1. 소셜 uuid 발급,
    2. 받은 uuid와 User 매칭
    3. 정보 저장
    4. 토큰 발급
    """
    def post(self, request):
        return ReturnResponse()


class SignOut(BaseModelViewSet):
    """
    로그아웃 부분
    1. 토큰 검증
    2. 받은 uuid의 refresh토큰 검증
    3. refresh 테이블 블랙리스트 등록
    4. 205 반환
    """
    def post(self, request):
        return ReturnResponse()
