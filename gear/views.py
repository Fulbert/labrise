from django.shortcuts import render, redirect, get_object_or_404

from gear.models import Gear, Brand
from member.models import Member

def home(request):
	pass

def show_gear(request, gear_pk):
	gear = get_object_or_404(Gear, pk=gear_pk)
	pilots = Member.objects.filter(gears=gear)
	context = {'gear':gear,'pilots':pilots}
	return render(request, 'gear/show_gear.html', context)

def show_brand(request, brand_pk):
	brand = get_object_or_404(Brand, pk=brand_pk)
	gears = Gear.objects.filter(brand=brand_pk)

	context = {'brand':brand,'gears':gears}
	return render(request, 'gear/show_brand.html', context)