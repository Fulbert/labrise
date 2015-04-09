from django.shortcuts import render
from flightlog.models import Trip

import datetime

def home(request):
	next_trip = Trip.objects.filter(date_start__gte=datetime.date.today())
	context = {'next_trip': next_trip}
	return render(request, 'flightlog/index.html', context)

def add_trip(request):
	pass
	#form = TripForm()
	#context = {'form': form}
	#return render(request, 'flightlog/add_trip.html', context)

def add_track(request):
	next_trip = Trip.objects.filter(date_start__gte=datetime.date.today())
	context = {'next_trip': next_trip}
	return render(request, 'flightlog/index.html', context)
