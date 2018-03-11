from django.contrib import admin

from studio.models import (Service, Room, BusinessHours, SpecialDay)

admin.site.register(Service)
admin.site.register(Room)
admin.site.register(BusinessHours)
admin.site.register(SpecialDay)
