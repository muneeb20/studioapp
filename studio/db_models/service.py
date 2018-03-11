from common.db_models import DatedModel
from django.db import models


class Service(DatedModel):
    name = models.CharField(max_length=100, verbose_name="Service Name")
    buffer_time = models.PositiveIntegerField(verbose_name="Buffer time in minutes")
    minimum_booking = models.PositiveIntegerField(verbose_name="Minimum booking in hours")

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.name

    def get_all_rooms(self):
        return self.room_set.all()

    def check_service_operating(self, start_time, end_time):
        weekday = start_time.weekday()
        return self.businesshours_set.filter(day=weekday, open_time__lt=start_time, close_time__gt=end_time).exists()
