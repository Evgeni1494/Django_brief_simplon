from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . views import Appointment
from django.forms import ModelForm

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('day','time','time_ordered','user','note')







