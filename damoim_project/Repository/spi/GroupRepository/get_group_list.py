from django.db.models import QuerySet, F
from damoim_service.models import Group


def get_group_list(user_id: int) -> QuerySet:
    return Group.objects.filter(grouptouser__user_id_id=user_id)
