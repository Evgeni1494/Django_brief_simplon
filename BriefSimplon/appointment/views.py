from django.shortcuts import render, redirect, get_object_or_404

from .forms import AppointmentForm, AddNote
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required
from .models import Appointment, Note



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


@login_required
def appointment_detail(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    notes = Note.objects.get(appointment=appointment_id)
    return render(request, 'appointment/appointment_detail.html', {'appointment': appointment, 'notes': notes})

@login_required
def add_note(request, appointment_id):
    if request.method == 'POST':
        form = AddNote(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
    
            return redirect('appointment_detail', appointment_id=appointment_id)
        # text = request.POST.get('text')
        # appointment = Appointment.objects.get(id=appointment_id)
        # Note.objects.create(appointment=appointment, text=text, created_by=request.user)
    else:
        form=AddNote() 
    return render(request, 'appointment/add_note.html',{'form':form})
    
    
