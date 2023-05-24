from django.shortcuts import render, redirect
from .forms import ApplicationForm

def application_for_admission(request):
	error = ''
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Форма была заполнена неверно' 

	form = ApplicationForm()

	data = {
		'form': form,
		'error': error
	}

	return render(request, 'application/application.html', data)
