from django.db.models import F, QuerySet


def get_user_list(group_id: int) -> QuerySet:
    from damoim_service.models import GroupToUser

    return GroupToUser.objects.filter(group_id_id=group_id).annotate(
        user_name=F("user_id__name"), user_thumbnail=F("user_id__thumbnail")
    )
