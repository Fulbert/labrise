from django.shortcuts import render
from flightlog.models import Trip
from flightlog.forms import TripForm

import datetime

def home(request):
	next_trip = Trip.objects.filter(date_start__gte=datetime.date.today())
	context = {'next_trip': next_trip}
	return render(request, 'flightlog/index.html', context)

def new_trip(request):
	form = TripForm()
	context = {'form': form}
	return render(request, 'flightlog/new_trip.html', context)

def new_track(request):
	next_trip = Trip.objects.filter(date_start__gte=datetime.date.today())
	context = {'next_trip': next_trip}
	return render(request, 'flightlog/index.html', context)
