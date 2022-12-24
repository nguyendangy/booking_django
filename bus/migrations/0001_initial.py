# Generated by Django 4.1.4 on 2022-12-24 16:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_number', models.IntegerField(default=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('number_reserved', models.PositiveSmallIntegerField()),
                ('transfer_date', models.DateTimeField()),
                ('transport_status', models.CharField(choices=[('FREE', 'Free'), ('SPACE', 'Space'), ('TRANSFER', 'Transfer'), ('ARRIVED', 'Arrived'), ('CANCELLED', 'Cancelled')], default='FREE', max_length=15)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('driver', models.CharField(max_length=50)),
                ('max_reservation', models.PositiveSmallIntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='BusAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must not consist of space and requires country code. eg : 989210000000', regex='^[1-9][0-9]{8,14}$')])),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('FREE', 'Free'), ('INVALID', 'Invalid'), ('RESERVED', 'Reserved')], default='FREE', max_length=10)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('Bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='bus.bus')),
                ('price', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.price')),
            ],
        ),
        migrations.CreateModel(
            name='BusReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_count', models.PositiveSmallIntegerField(default=0)),
                ('children_count', models.PositiveSmallIntegerField(default=0)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bus_reservation', to='bus.busseat')),
                ('total_cost', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reservations.price')),
            ],
        ),
    ]
