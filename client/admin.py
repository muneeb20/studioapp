from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from client.models import Client


class ClientModelAdmin(ModelAdmin):
    model = Client

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return 'first_name', 'last_name', 'full_name', 'contact_number', 'email'


admin.site.register(Client, ClientModelAdmin)
