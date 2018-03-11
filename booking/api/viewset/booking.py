from booking.api.serializers import BookingSerializer
from rest_framework import viewsets


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = BookingSerializer.Meta.model.objects.all()
