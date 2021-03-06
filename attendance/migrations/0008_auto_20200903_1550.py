# Generated by Django 3.0.5 on 2020-09-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_semesters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=100)),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.FacultyData')),
            ],
        ),
        migrations.DeleteModel(
            name='SubjectData',
        ),
    ]
