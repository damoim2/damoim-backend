from dataclasses import dataclass

from damoim_service.models import User


@dataclass
class CreatePostCommand:
    user_id: User
    group_id_id: int
    title: str
    contents: str
