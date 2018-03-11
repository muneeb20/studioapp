from booking.api.viewset import BookingViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'bookings', BookingViewSet, base_name='booking')
