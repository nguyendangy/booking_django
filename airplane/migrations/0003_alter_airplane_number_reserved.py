# Generated by Django 4.1.4 on 2022-12-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airplane', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='number_reserved',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
