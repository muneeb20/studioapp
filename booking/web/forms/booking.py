from booking.api.serializers import BookingSerializer
from django import forms
from django.core.validators import EmailValidator
from rest_framework.exceptions import ValidationError
from studio.models import Service


class BookingForm(forms.Form):
    SERIALIZER_CLASS = BookingSerializer

    first_name = forms.CharField(required=True, max_length=30, min_length=2,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=30, min_length=2,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    contact_number = forms.CharField(required=True, max_length=30, min_length=8,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Contact Number',
                                                'type': 'number'}))
    email = forms.EmailField(required=True, max_length=30,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             validators=[EmailValidator])
    start_time = forms.CharField(required=True,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Start Time',
                                                'type': 'datetime-local'}))
    end_time = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'End Time',
                                              'type': 'datetime-local'}))

    service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Select Service'}))

    def is_valid_booking_info(self):
        try:
            self.serializer = self.SERIALIZER_CLASS(data=self.reformat_request_data(self.data.dict()))
            self.serializer.is_valid(raise_exception=True)
        except Exception as ex:
            return ex

    def save(self):
        self.serializer.save()

    def reformat_request_data(self, dict_data):
        json_dict_api = {}
        json_dict_api['client'] = {'first_name': dict_data.get('first_name'),
                                   'last_name': dict_data.get('last_name'),
                                   'email': dict_data.get('email'),
                                   'contact_number': dict_data.get('contact_number')}
        json_dict_api['start_time'] = dict_data.get('start_time')
        json_dict_api['end_time'] = dict_data.get('end_time')
        json_dict_api['service'] = {'id': dict_data.get('service')}
        return json_dict_api
