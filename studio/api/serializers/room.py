from rest_framework import serializers

from studio.models import Room


class RoomSerializer(serializers.ModelSerializer):
    # service = serializers.HyperlinkedRelatedField(view_name='studio:service-detail', read_only=True, lookup_field='id')

    class Meta:
        model = Room
        fields = ('id', 'name', 'service')
