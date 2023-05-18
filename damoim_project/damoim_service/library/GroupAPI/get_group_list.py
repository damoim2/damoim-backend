from Repository.spi.GroupRepository import get_group_list as read_group_list


def get_group_list(user_id: int):
    return read_group_list(user_id=user_id).values("index", "name", "thumbnail")
