from common.db_models import DatedModel
from django.db import models

from .service import Service


class BusinessHours(DatedModel):
    WEEKDAYS = ((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'),
                (6, 'Sunday'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    day = models.SmallIntegerField(choices=WEEKDAYS)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        db_table = "business_hour"

    def __str__(self):
        return self.get_day_display()
