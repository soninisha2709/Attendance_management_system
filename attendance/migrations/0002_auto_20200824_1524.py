# Generated by Django 3.0.5 on 2020-08-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='std_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
