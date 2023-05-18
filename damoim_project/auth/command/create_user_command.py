from dataclasses import dataclass


@dataclass
class CreateUserCommand:
    username: str
    password: str
    uuids: int
    name: str
