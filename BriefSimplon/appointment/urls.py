from django.urls import path,include
from . import views

app_name = 'appointment'

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('new_appointment/',views.new_appointment, name='new_appointments'),
    
]