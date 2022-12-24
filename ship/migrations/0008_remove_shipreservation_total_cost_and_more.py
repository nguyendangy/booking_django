# Generated by Django 4.1.4 on 2022-12-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0007_shipreservation_reserved_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipreservation',
            name='total_cost',
        ),
        migrations.AlterField(
            model_name='shipreservation',
            name='reserved_status',
            field=models.CharField(choices=[('INITIAL', 'Initial'), ('RESERVED', 'Reserved'), ('CANCELLED', 'Cancelled'), ('FINISHED', 'Finished'), ('PROBLEM', 'Problem')], default='INITIAL', max_length=15),
        ),
    ]
