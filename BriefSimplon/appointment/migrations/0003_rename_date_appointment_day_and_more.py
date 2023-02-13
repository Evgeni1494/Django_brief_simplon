# Generated by Django 4.1.6 on 2023-02-13 11:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0002_alter_appointment_date_alter_appointment_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_note',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_phone',
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_ordered',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('9 h', '9h'), ('9h55', '9h55'), ('10h50', '10h50'), ('11h45', '11h45'), ('13h30', '13h30'), ('14h25', '14h25'), ('15h20', '15h20'), ('16h15', '16h15')], default='3 PM', max_length=10),
        ),
    ]