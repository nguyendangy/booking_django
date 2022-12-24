# Generated by Django 4.1.4 on 2022-12-24 18:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airplane', '0006_airplanereservation_reserved_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplanereservation',
            name='reserved_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
