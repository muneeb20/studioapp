from common.db_models import DatedModel
from django.db import models

from .service import Service


class SpecialDay(DatedModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    close_datetime = models.DateTimeField(verbose_name="Day on which studio is closed")
    reason = models.CharField(max_length=200)

    class Meta:
        db_table = "special_off_days"

    def __str__(self):
        return self.service.name + " : " + self.reason
