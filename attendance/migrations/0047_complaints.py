# Generated by Django 3.0.5 on 2020-09-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0046_delete_complain_manage'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('std_id', models.CharField(max_length=10, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Student_Data'))),
                ('msg', models.CharField(max_length=250)),
            ],
        ),
    ]
