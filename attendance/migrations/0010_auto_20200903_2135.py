# Generated by Django 3.0.5 on 2020-09-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_auto_20200903_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semesters',
            old_name='std_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='f_id',
            new_name='faculty',
        ),
    ]
