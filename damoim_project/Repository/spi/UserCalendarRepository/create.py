from damoim_service.models import UserCalendar


def create(kwargs):
    """
    user_id=command.user_id,
    from_date=command.from_date,
    to_date=command.to_date,
    time=command.time,
    title=command.title,
    address=command.address,
    memo=command.memo,
    icon_id=command.icon_id,
    color=command.color,
    is_day_on=command.is_day_on,
    """

    return UserCalendar.objects.create(**kwargs)