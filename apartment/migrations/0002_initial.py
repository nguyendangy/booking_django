# Generated by Django 4.1.4 on 2022-12-24 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartmentrating',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='apartment.apartment'),
        ),
        migrations.AddField(
            model_name='apartmentrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartmentaddress',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='reservations.location'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='apartment_address', to='apartment.apartmentaddress'),
        ),
        migrations.AddConstraint(
            model_name='apartmentroom',
            constraint=models.UniqueConstraint(fields=('apartment', 'number'), name='unique_apartment_number_seat'),
        ),
        migrations.AddConstraint(
            model_name='apartmentreservation',
            constraint=models.UniqueConstraint(fields=('user', 'room'), name='unique_user_apartment_room'),
        ),
        migrations.AddConstraint(
            model_name='apartmentrating',
            constraint=models.UniqueConstraint(fields=('apartment', 'user', 'rate'), name='unique_apartment_user_rate'),
        ),
        migrations.AddConstraint(
            model_name='apartment',
            constraint=models.UniqueConstraint(fields=('name', 'residence_status'), name='unique_apartment_name_residence_status'),
        ),
    ]
