from django.db import models
from datetime import datetime
from BriefSimplon import settings
from django.contrib.auth.models import User
from django import forms
TIME_CHOICES = (
                        ("9 h", "9h"),
                        ("9h55", "9h55"),
                        ("10h50", "10h50"),
                        ("11h45", "11h45"),
                        ("13h30", "13h30"),
                        ("14h25", "14h25"),
                        ("15h20", "15h20"),
                        ("16h15", "16h15"),
            )

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True)

    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    note = models.TextField(max_length=900, default='')

    def str(self):
        return f"{self.user} | day: {self.day} | time: {self.time} | name :{self.user} | note:{self.note}"
    def notes(self):
        return Note.objects.filter(appointment=self)
    
class Note(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_notes')
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def str(self):
        return f"{self.appointment} | Note: {self.text}"

    
    
    
