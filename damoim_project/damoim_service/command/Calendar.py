import datetime
from dataclasses import dataclass


@dataclass
class CreateGroupScheduleCommand:
    group_id: int
    from_date: datetime.datetime
    to_date: datetime.datetime
    time: datetime.time
    title: str
    address: str
    memo: str
    icon_id: int
    color: str
    is_day_on: bool


@dataclass
class CreateUserScheduleCommand:
    user_id: int
    from_date: datetime.datetime
    to_date: datetime.datetime
    time: datetime.datetime
    title: str
    address: str
    memo: str
    icon_id: int
    color: str
    is_day_on: bool
