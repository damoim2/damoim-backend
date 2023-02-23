from dataclasses import dataclass


@dataclass
class UserData:
    def get_uuid(self) -> str:
        raise NotImplementedError()


@dataclass
class UserSet(UserData):
    username: str
    password: str
    uuids: int

    def get_uuid(self) -> str:
        return self.uuids
