from rest_framework_simplejwt import views as jwt_views
from user.port.api import UserServiceUseCase


class UserLoginView(jwt_views.TokenObtainPairView):
    def __init__(self, usecase: UserServiceUseCase) -> None:
        self.user_service_usecase = usecase
        super().__init__()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
