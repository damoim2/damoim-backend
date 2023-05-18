from dataclasses import dataclass

from django.core.files import File


@dataclass
class CreateGroup:
    user_id: int
    name: str
    files: File
