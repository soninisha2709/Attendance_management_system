# Generated by Django 3.0.5 on 2020-09-10 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0052_auto_20200909_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='complain_table',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('Std', models.CharField(max_length=10, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Student_Data'))),
                ('msg', models.CharField(max_length=250)),
            ],
        ),
    ]
