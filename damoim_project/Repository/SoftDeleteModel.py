from django.db import models
from django.utils import timezone
from .SoftDeleteManager import SoftDeleteManager


class SoftDeleteModel(models.Model):
    # Field name made lowercase.
    deletedat = models.DateTimeField(db_column="deleted_at", blank=True, null=True)

    class Meta:
        abstract = True  # 상속 할수 있게

    objects = SoftDeleteManager()  # 커스텀 매니저
    objects_all = models.Manager()  # 매니저

    def delete(self, using=None, keep_parents=False):
        self.deletedat = timezone.now()
        self.save(update_fields=["deletedat"])

    def hard_delete(self):
        try:
            super(SoftDeleteModel, self).delete()
        except Exception as e:
            pass

    def restore(self):  # 삭제된 레코드를 복구한다.
        self.deletedat = None
        self.save(update_fields=["deletedat"])
