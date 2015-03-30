from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

def login(request):
	if request.method == 'POST':
		form = request.POST

		user = authenticate(username=form.username, password=form.password)
		if user is not None:
			if user.is_active:
				return redirect('page.views.home')
			else:
				return redirect('page.views.home')
		else:
			return redirect('page.views.home')

	else:
		form = AuthenticationForm(request)
		context = {'form': form}
		return render(request,'util/login.html',context)
