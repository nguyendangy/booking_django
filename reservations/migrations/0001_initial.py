# Generated by Django 4.1.4 on 2022-12-24 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coordination', models.FloatField(blank=True, null=True)),
                ('y_coordination', models.FloatField(blank=True, null=True)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('ratio', models.FloatField(default=0.0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='reservations.currency')),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('currency_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_from', to='reservations.currency')),
                ('currency_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_to', to='reservations.currency')),
            ],
        ),
        migrations.AddConstraint(
            model_name='currencyexchangerate',
            constraint=models.UniqueConstraint(fields=('currency_from', 'currency_to'), name='unique_currency_from_currency_to'),
        ),
        migrations.AddConstraint(
            model_name='currencyexchangerate',
            constraint=models.CheckConstraint(check=models.Q(('currency_from', models.F('currency_to')), _negated=True), name='currency_from_and_currency_to_not_be_equal'),
        ),
    ]
