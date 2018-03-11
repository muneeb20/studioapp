from client.models import Client
from rest_framework.serializers import ModelSerializer


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email')
