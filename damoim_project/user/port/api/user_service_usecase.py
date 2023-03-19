from typing import Protocol
from user.domain.model.login_user import UserLoginCommand


class UserServiceUseCase(Protocol):
    def user_service(self, command: UserLoginCommand):
        pass
