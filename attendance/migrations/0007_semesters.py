# Generated by Django 3.0.5 on 2020-09-03 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_subjectdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=10)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.StudentData')),
            ],
        ),
    ]
