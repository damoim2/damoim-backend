from django.db import models


class SoftDeleteManager(models.Manager):
    # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deletedat__isnull=True)
