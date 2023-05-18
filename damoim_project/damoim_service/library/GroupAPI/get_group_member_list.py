from Repository.spi.GroupToUserRepository import get_user_list


def get_group_member_list(group_id: int) -> list:
    return get_user_list(group_id=group_id).values(
        "user_name", "user_thumbnail", "user_id_id"
    )
