# Generated by Django 3.0.5 on 2020-09-05 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0020_auto_20200905_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceTable',
            fields=[
                ('att_id', models.AutoField(primary_key=True, serialize=False)),
                ('std_id', models.CharField(max_length=100, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Semesters'))),
                ('sub_id', models.CharField(max_length=100, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Subjects'))),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance_Master_table',
        ),
    ]
