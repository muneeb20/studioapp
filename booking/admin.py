from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from booking.models import Booking


class BookingModelAdmin(ModelAdmin):
    model = Booking

    def get_readonly_fields(self, request, obj=None):
        return 'client', 'room', 'booking_reference', 'start_time', 'end_time', 'user'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BookingModelAdmin, self).save_model(request, obj, form, change)


admin.site.register(Booking, BookingModelAdmin)
