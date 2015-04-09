from django.shortcuts import render

from space.models import Point

def home(request):
	points = Point.objects.all()
	context = {'points':points}
	return render(request, 'space/home.html', context)