import uuid

from client.models import Client
from common.db_models import DatedModel
from django.contrib.auth.models import User
from django.db import models
from studio.models import Room


class Booking(DatedModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_reference = models.CharField(max_length=30, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_accepted = models.BooleanField(default=False)

    class Meta:
        db_table = "booking"

    def __str__(self):
        return self.booking_reference + ": " + self.client.email

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.booking_reference = uuid.uuid4().hex[:10].upper()
        super(Booking, self).save()
