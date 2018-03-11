from rest_framework.viewsets import ReadOnlyModelViewSet
from studio.api.serializers import RoomSerializer


class RoomViewSet(ReadOnlyModelViewSet):
    serializer_class = RoomSerializer
    queryset = RoomSerializer.Meta.model.objects.all()
