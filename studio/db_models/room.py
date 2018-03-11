from common.db_models import DatedModel
from django.db import models

from .service import Service


class Room(DatedModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Room Name")

    class Meta:
        db_table = "room"

    def __str__(self):
        return self.service.name + " : " + self.name
