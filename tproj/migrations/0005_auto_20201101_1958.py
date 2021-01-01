# Generated by Django 2.0.13 on 2020-11-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tproj', '0004_auto_20201101_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_station',
            field=models.IntegerField(choices=[(1, 'AHMEDABAD'), (2, 'CHENNAI'), (3, 'MUMBAI'), (4, 'PUNE'), (5, 'KOLKATA'), (6, 'THIRUVANANTHAPURAM'), (7, 'HYDERABAD'), (8, 'BENGALURU'), (9, 'PONDICHERRY'), (10, 'GANDHINAGAR')], default=1),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_station',
            field=models.IntegerField(choices=[(1, 'AHMEDABAD'), (2, 'CHENNAI'), (3, 'MUMBAI'), (4, 'PUNE'), (5, 'KOLKATA'), (6, 'THIRUVANANTHAPURAM'), (7, 'HYDERABAD'), (8, 'BENGALURU'), (9, 'PONDICHERRY'), (10, 'GANDHINAGAR')], default=1),
        ),
    ]