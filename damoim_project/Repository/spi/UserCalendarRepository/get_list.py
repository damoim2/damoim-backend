import datetime
import calendar
from damoim_service.models import UserCalendar
from django.utils import timezone


def get_list(command):
    today = timezone.now()
    now_month_start = datetime.datetime(year=today.year, month=today.month, day=1)
    now_month_end = datetime.datetime(
        year=today.year,
        month=today.month,
        day=calendar.monthrange(year=today.year, month=today.month)[1],
    )
    return UserCalendar.objects.filter(
        from_date__gte=now_month_start,
        from_date__lte=now_month_end,
        user_id_id=command.user_id,
    )
