from damoim_project.user.adapter.spi.entity.User import User
from django.db.models import QuerySet, Model
from damoim_project.user.adapter.spi.serializer import CreateUserSerializer
from damoim_project.user.domain.model.UserSet import UserSet


class UserRepository:
    origin = User

    def find_user_by_uuid(self, uuid: int) -> QuerySet(model=User):
        return self.origin.objects.get(uuid=uuid)

    def find_user_by_username(self, username: str) -> int:
        return self.origin.objects.get(username=username).uuid

    def save_user(self, user_set: UserSet) -> bool:
        instance = self.user_set_to_entity(user_set=user_set)
        serializer = CreateUserSerializer(data=instance)
        if serializer.is_valid():
            return True
        else:
            return False

    def user_set_to_entity(self, user_set: UserSet) -> dict:
        return {"username": user_set.username, "password": user_set.password}
