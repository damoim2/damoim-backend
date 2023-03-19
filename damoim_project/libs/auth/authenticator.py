from rest_framework.authentication import TokenAuthentication
from libs.Logger import Logging
from libs.auth.Token import Token
from user.models import User
logger = Logging("AUTH")

# 해당 Auth부분은 middleware 작동이 끝나고 rest-framework 레이어에 도달하자마자 실행되는 인증 함수임
class Authentication(TokenAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if auth_header is None:
            # access token이 없을 때, 처리
            return
        success, user = self.conn_auth_server(access_token=auth_header)
        if success:
            # access token 디코드 시
            request.user = user
            return user, auth_header
        else:
            # access token 디코드 실패 시 (expire 경우)
            return

    def conn_auth_server(self,access_token: str):
        """
        Verify 구문 들어가야함
        """
        decode_object = Token().decode_and_verify_access_token(access_token)

        if decode_object is not None:
            user_instance = User.objects.get(user_id=decode_object['user_id'])
            return True, user_instance
        else:
            return False, None
