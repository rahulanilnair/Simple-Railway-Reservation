# Generated by Django 2.0.13 on 2020-10-30 05:56

from django.db import migrations, models
import django.db.models.deletion
import tproj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets_number', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100, null=True, validators=[tproj.models.validate_string])),
                ('middle_name', models.CharField(max_length=100, null=True, validators=[tproj.models.validate_string])),
                ('last_name', models.CharField(max_length=100, null=True, validators=[tproj.models.validate_string])),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('passengers', models.ManyToManyField(to='tproj.Passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_date', models.DateTimeField()),
                ('end_time_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('end_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_station', to='tproj.Station')),
                ('start_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_station', to='tproj.Station')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trip_train', to='tproj.Train')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tproj.Trip'),
        ),
    ]
