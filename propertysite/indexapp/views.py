from django.shortcuts import render, redirect

from indexapp.forms import CreateContactUSForm
# Create your views here.


# Create your views here.
def index(request):
	return render(request, 'indexapp/index.html', {})

def properties(request):
	return render(request, 'indexapp/properties.html', {})


def about(request):
	return render(request, 'indexapp/about.html', {})

def services(request):
	return render(request, 'indexapp/services.html', {})

def contact(request):
	contact_us_form = CreateContactUSForm()
	if request.method == 'POST':
		contact_us_form = CreateContactUSForm(request.POST)
		if contact_us_form.is_valid():
			contact_us_form.save()
			return redirect('index')
	diction = {'form':contact_us_form}
	return render(request, 'indexapp/contact.html', context=diction)