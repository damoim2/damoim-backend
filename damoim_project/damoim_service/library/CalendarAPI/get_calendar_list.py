from Repository.spi import GroupCalendarRepository, UserCalendarRepository
from Repository.spi.GroupRepository import get_group_list


def get_calendar_list(command):
    UserCalendarRepository.get_list(command)
    group_list = get_group_list(command.user_id)
    GroupCalendarRepository.get_list(command)
    return
