from django.http.response import HttpResponseRedirect

from booking.web.forms import BookingForm
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import View


class BookingView(View):
    form_class = BookingForm
    template_name = 'booking.html'

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        errors = None
        if form.is_valid():
            errors = form.is_valid_booking_info()
            if not errors:
                form.save()
        errors = form.errors or errors
        if not errors:
            messages.success(request, 'Form submission successful. We will contact you soon.')
            return HttpResponseRedirect(redirect_to='/')
        return render(request, self.template_name, {'form': form, 'errors': errors})
