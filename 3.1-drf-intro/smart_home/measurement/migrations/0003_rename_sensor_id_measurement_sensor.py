# Generated by Django 4.2 on 2023-05-20 09:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0002_alter_sensor_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="measurement",
            old_name="sensor_id",
            new_name="sensor",
        ),
    ]