# Generated by Django 4.0 on 2024-04-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidents',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='incidents',
            name='time_end',
        ),
        migrations.RemoveField(
            model_name='incidents',
            name='time_start',
        ),
    ]