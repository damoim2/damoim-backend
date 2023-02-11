from user.port.api.user_service_usecase import UserServiceUseCase
from user.domain.model.login_user import UserLoginCommand

class UserService(UserServiceUseCase):
    def user_service(self, command: UserLoginCommand):
        return 