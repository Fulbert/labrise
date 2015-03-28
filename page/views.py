from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    latest_users = User.objects.order_by('-date_joined')[:5]
    context = {'latest_users': latest_users}
    return render(request, 'index.html', context)