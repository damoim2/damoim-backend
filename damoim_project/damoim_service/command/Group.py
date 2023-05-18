from dataclasses import dataclass


@dataclass
class CreateGroupCommand:
    name: str
    owner: int
    thumbnail: str
