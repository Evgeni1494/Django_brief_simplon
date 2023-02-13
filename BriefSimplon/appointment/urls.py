from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('new_appointment/',views.new_appointment, name='new_appointments'),
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/<int:appointment_id>/add_note/', views.add_note, name='add_note'),
]