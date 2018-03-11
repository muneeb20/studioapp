from common.db_models import DatedModel
from django.db import models


class Client(DatedModel):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    full_name = models.CharField(max_length=200, verbose_name="First Name")
    contact_number = models.CharField(max_length=20, verbose_name="contact number of client")
    email = models.EmailField(max_length=30, verbose_name="client email", unique=True, db_index=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.email

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_name = self.first_name + " " + self.last_name
        super(Client, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)

    @classmethod
    def get_or_return_none(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist as e:
            return None

    @classmethod
    def get_or_create_client(cls, client_data):
        client = cls.get_or_return_none(client_data.get('email'))
        if client is None:
            client, created = cls.objects.get_or_create(**client_data)
        return client
