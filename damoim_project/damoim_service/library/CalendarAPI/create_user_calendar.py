from Repository.spi.UserCalendarRepository.create import create
from dataclasses import asdict


def create_user_schedule(command):
    return create(asdict(command))
