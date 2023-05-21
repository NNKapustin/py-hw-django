# Generated by Django 4.2 on 2023-05-21 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0003_rename_sensor_id_measurement_sensor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="sensor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="measurements",
                to="measurement.sensor",
            ),
        ),
    ]
