from dataclasses import dataclass
from django.utils import timezone


@dataclass
class CreateGroupToUserCommand:
    user_id: int
    group_id: int
