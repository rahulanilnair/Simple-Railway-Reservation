from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
def validate_string(value):
    if value.isalpha():
        print('Good')
    else:
        raise ValidationError(
            ('Enter a valid name!'),
            params={'value': value},
        )

class Station(models.Model):
    name = models.CharField(null=True, max_length=100)
    def __str__(self):
        return "{}".format(self.name)




class Train(models.Model):
    name = models.CharField(null=True, max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)



class Trip(models.Model):
    train = models.ForeignKey(Train, related_name="trip_train", null=True, on_delete=models.CASCADE)
    start_station = models.ForeignKey(Station, related_name="start_station" ,on_delete=models.CASCADE, null=True)
    end_station = models.ForeignKey(Station, related_name="end_station" ,on_delete=models.CASCADE, null=True)
    start_time_date = models.DateTimeField()
    end_time_date = models.DateTimeField()
    


    def __str__(self):
        return "Start: {} - End: {} - Train: {}".format(self.start_station, self.end_station, self.train)



class Passenger(models.Model):
    SEAT_NUMBER = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
        (13,'13'),
        (14,'14'),
        (15,'15'),
        (16,'16'),
        (17,'17'),
        (18,'18'),
        (19,'19'),
        (20,'20'),
        (21,'21'),
        (22,'22'),
        (23,'23'),
    )
    seat_number = models.IntegerField(default=1, choices=SEAT_NUMBER)
    #ticket_ptr = models.OneToOneField(null=True, auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=False, serialize=False, to='details.Ticket')
    def __str__(self):
        return "{}".format(self.seat_number)



class Ticket(models.Model):
    GENDER = (
        ('O', 'Other'),
        ('M', 'Male'),
        ('F','Female')
    )

    trip = models.ForeignKey(Trip, related_name="tickets", null=True, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True, blank=True)
    first_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    middle_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    last_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    email = models.EmailField(max_length=70,blank=True, null= True)
    gender = models.CharField(choices=GENDER,default='O',max_length=5)
    seat = models.ManyToManyField(Passenger)

    def __str__(self):
        return "{}".format(self.first_name)

# Create your models here.
