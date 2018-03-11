from rest_framework import routers

from studio.api.viewsets import (ServiceViewSet, RoomViewSet)

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet, base_name='service')
router.register(r'rooms', RoomViewSet, base_name='rooms')
