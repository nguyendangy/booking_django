# Generated by Django 4.1.4 on 2022-12-24 17:04

from django.db import migrations, models
import utlis.validation_transport_date


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_remove_bus_unique_driver_transport_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='transfer_date',
            field=models.DateTimeField(validators=[utlis.validation_transport_date.validation_transport_date]),
        ),
    ]
