from django.db import models


class DatedModel(models.Model):
    """
        Base model for models where we need to store creation and last modification timestamp of object
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
