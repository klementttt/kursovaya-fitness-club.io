from django import forms
from .models import Appointment, Booking

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['trainer', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
