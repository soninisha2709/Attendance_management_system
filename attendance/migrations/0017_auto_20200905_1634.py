# Generated by Django 3.0.5 on 2020-09-05 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_fill_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fill_attendance',
            name='attendance',
        ),
        migrations.DeleteModel(
            name='attendance_master',
        ),
        migrations.DeleteModel(
            name='fill_attendance',
        ),
    ]
