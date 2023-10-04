from django.shortcuts import render, redirect
from webapp.forms import PropertyEntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def propertyentryform(request):
    form_entry = PropertyEntryForm()
    if request.method == 'POST':
        form_entry = PropertyEntryForm(request.POST, request.FILES)
        if form_entry.is_valid():
            form_entry.save()
            return redirect('index')
    diction = {'form_entry': form_entry}
    return render(request, 'webapp/propertyentry.html', context=diction)


