from Repository.spi.GroupCalendarRepository.create import create
from dataclasses import asdict


def create_group_schedule(command):
    return create(asdict(command))
