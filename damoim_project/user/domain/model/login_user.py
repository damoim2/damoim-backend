from dataclasses import dataclass


@dataclass
class UserCommand:
    pass


@dataclass
class UserLoginCommand(UserCommand):
    username: str
    password: str
