from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Ticket, Trip , Station , Passenger , Train
from django.http import Http404
from django.shortcuts import get_object_or_404
from .forms import PassengerForm,TripForm, TicketForm
from django.contrib.auth.decorators import login_required
import logging

# Get an instance of a logger
#logger = logging.getLogger(__name__)
@login_required
def home_page(request):
    return render(request,'details/base.html',)

@login_required
def passenger_new(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.save()
            return redirect('trip_new', pk=passenger.pk)
    else:
        form = PassengerForm()
    return render(request, 'details/passenger.html', {'form': form})

@login_required
def trip_new(request,pk):
    if request.method == "POST":
        form=TripForm(request.POST)
        if form.is_valid():
            trip=form.save(commit=False)
            trip.save()
            return redirect('ticket_new',pk=trip.pk)
    else:
        form=TripForm()
    return render(request, 'details/trip.html', {'form': form})

@login_required
def ticket_new(request,pk):
    if request.method == "POST":
        form=TicketForm(request.POST)
        if form.is_valid():
            ticket=form.save(commit=True)
            ticket.save()
    else:
        form=TicketForm()
    return render(request, 'details/ticket.html', {'form': form})



    

