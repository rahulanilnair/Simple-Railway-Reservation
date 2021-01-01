from django import forms
from .models import Passenger
from .models import Station
from .models import Train
from .models import Trip
from .models import Ticket

class PassengerForm(forms.ModelForm):
    class Meta:
        model=Passenger
        fields=('seat_number',)


class TripForm(forms.ModelForm):
    class Meta:
        model=Trip
        fields=('train','start_station','end_station','start_time_date','end_time_date',)
    
class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=('trip','first_name','middle_name','last_name','email','gender','seat',)
        