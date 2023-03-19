from django.db import models
from django.utils import timezone
class SoftDeleteManager(models.Manager):
    # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deletedat__isnull=True)


class SoftDeleteModel(models.Model):
    # Field name made lowercase.
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True  # 상속 할수 있게

    objects = SoftDeleteManager()  # 커스텀 매니저
    objects_all = models.Manager()  # 매니저

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def hard_delete(self):
        try:
            super(SoftDeleteModel, self).delete()
        except Exception as e:
            pass

    def restore(self):  # 삭제된 레코드를 복구한다.
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])
