# Generated by Django 4.1.4 on 2022-12-24 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shiprating',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='ship.ship'),
        ),
        migrations.AddField(
            model_name='shiprating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shipaddress',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='reservations.location'),
        ),
        migrations.AddField(
            model_name='ship',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='destination', to='ship.shipaddress'),
        ),
        migrations.AddField(
            model_name='ship',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='source', to='ship.shipaddress'),
        ),
        migrations.AddConstraint(
            model_name='shipseat',
            constraint=models.UniqueConstraint(fields=('ship', 'number'), name='unique_ship_seat'),
        ),
        migrations.AddConstraint(
            model_name='shipreservation',
            constraint=models.UniqueConstraint(fields=('user', 'seat'), name='unique_user_ship_seat'),
        ),
        migrations.AddConstraint(
            model_name='shiprating',
            constraint=models.UniqueConstraint(fields=('ship', 'user', 'rate'), name='unique_ship_user_rate'),
        ),
        migrations.AddConstraint(
            model_name='ship',
            constraint=models.UniqueConstraint(condition=models.Q(('transport_status__in', ['FREE', 'SPACE', 'TRANSFER'])), fields=('captain', 'transport_status'), name='unique_captain_status'),
        ),
    ]
