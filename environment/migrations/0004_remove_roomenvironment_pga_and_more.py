# Generated by Django 4.2 on 2023-04-18 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0003_alter_roomenvironment_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomenvironment',
            name='pga',
        ),
        migrations.RemoveField(
            model_name='roomenvironment',
            name='seismic_intensity',
        ),
        migrations.RemoveField(
            model_name='roomenvironment',
            name='si_value',
        ),
        migrations.RemoveField(
            model_name='roomenvironment',
            name='vibration_information',
        ),
    ]