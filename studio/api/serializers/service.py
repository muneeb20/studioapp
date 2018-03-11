from rest_framework.serializers import ModelSerializer

from studio.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')
