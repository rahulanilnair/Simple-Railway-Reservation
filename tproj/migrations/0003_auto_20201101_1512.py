# Generated by Django 2.0.13 on 2020-11-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tproj', '0002_remove_trip_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='gender',
            field=models.IntegerField(choices=[(1, 'unspecified'), (2, 'male'), (3, 'female')], default=1, max_length=1),
        ),
    ]
