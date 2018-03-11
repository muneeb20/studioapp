from datetime import timedelta, datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from booking.models import Booking
from client.api.serializers import ClientSerializer
from studio.api.serializers.service import ServiceSerializer


class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    booking_reference = serializers.CharField(required=False, read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('booking_reference', 'start_time', 'end_time', 'is_accepted', 'client', 'service')

    def create(self, validated_data):
        """
        Create method for serializer is overidden to support nested writable serializer.
        :param validated_data:
        :return booking object:
        """
        client_data = self.initial_data.get('client')
        client_instance = ClientSerializer.Meta.model.get_or_create_client(client_data)
        validated_data.update({'client': client_instance, 'room_id': self.room_id})
        return Booking.objects.create(**validated_data)

    def is_valid(self, raise_exception=False):
        """
        is valid is overridden to write custom validations for the input payload
        :param raise_exception:
        :return boolean:
        """
        is_valid = super(BookingSerializer, self).is_valid(raise_exception=raise_exception)
        return is_valid and self.check_room_is_available_and_assign_room()

    def check_room_is_available_and_assign_room(self):
        """
        This method handle all data input validation. Make sure we have timeslot available in that specific time.
        :return boolean:
        """
        service = self.check_is_valid_service()
        start_time, end_time = self.is_valid_datetime_provided()
        if (end_time - start_time).seconds / 3600 < service.minimum_booking:
            raise ValidationError("Minimum booking is %s hours" % (str(service.minimum_booking)))
        if service.check_service_operating(start_time, end_time):
            raise ValidationError("Sorry we are busy in these times")
        start_time_with_buffer = start_time - timedelta(minutes=service.buffer_time)
        end_time_with_buffer = end_time + timedelta(minutes=service.buffer_time)
        bookings_at_same_time = Booking.objects.filter(start_time__gte=start_time_with_buffer,
                                                       end_time__lte=end_time_with_buffer)
        if bookings_at_same_time:
            raise ValidationError("Request service not available at given time. Please choose another time")
        self.room_id = service.get_all_rooms().first().id
        return True

    def check_is_valid_service(self):
        """
        Check where service exist in system or not
        :return service object:
        """
        try:
            return ServiceSerializer.Meta.model.objects.get(id=self.initial_data.get('service', {}).get('id'))
        except ServiceSerializer.Meta.model.DoesNotExist:
            raise ValidationError("Invalid Service Id provided")

    def is_valid_datetime_provided(self):
        """
        This method validates that start_time are correct.
        :return start_time, end_time in datetime format:
        """
        try:
            start_time = datetime.strptime(self.initial_data.get('start_time'), '%Y-%m-%dT%H:%M')
            end_time = datetime.strptime(self.initial_data.get('end_time'), '%Y-%m-%dT%H:%M')
            if datetime.now() > start_time or datetime.now() > end_time or start_time.date() != end_time.date():
                raise ValidationError("Invalid start and end time provided")
            return start_time, end_time
        except Exception as e:
            raise ValidationError("Invalid format for start or end time must follow this format, 'YYYY-mm-dd HH:MM")
