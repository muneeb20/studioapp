from rest_framework.viewsets import ReadOnlyModelViewSet
from studio.api.serializers import ServiceSerializer


class ServiceViewSet(ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer
    queryset = ServiceSerializer.Meta.model.objects.all()
