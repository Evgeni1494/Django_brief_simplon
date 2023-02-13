from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/appointments.html', {'appointments': appointments})

def new_appointment(request):
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment=form.save()
            appointment.save()
            return redirect('/appointments')
        else:
            print("Mal Rempli")
    else:
        appointment = AppointmentForm()
        print("Rendezvous confirmé")
    
    return render(request, 'appointment/new_appointment.html',{'form':appointment})


    
    
