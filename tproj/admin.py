from django.contrib import admin
from .models import Passenger
from .models import Station
from .models import Ticket
from .models import Train
from .models import Trip
# Register your models here.
admin.site.register(Passenger)
admin.site.register(Station)
admin.site.register(Ticket)
admin.site.register(Train)
admin.site.register(Trip)