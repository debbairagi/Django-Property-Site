from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from indexapp.models import ContactUSMessage
from userapp.models import Agent


# Create your views here.
@login_required(login_url='userapp_login')
def dashboard(request):
    return render(request, 'crudapp/dashboard.html', {})


@login_required(login_url='userapp_login')
def view_contact_message(request):
    contact_messages = ContactUSMessage.objects.all()
    diction = {'contact_messages':contact_messages}
    return render(request, 'crudapp/view_contact_messages.html', context=diction)

@login_required(login_url='userapp_login')
def view_single_message(request, pk):
    msgs = ContactUSMessage.objects.get(id=pk)
    diction =  {'msgs': msgs}
    return render(request, 'crudapp/view_single_message.html', context=diction)

@login_required(login_url='userapp_login')
def view_agent(request):
    agents = Agent.objects.all()
    diction = {'agents': agents}
    return render(request, 'crudapp/view_agent.html', context=diction)

@login_required(login_url='userapp_login')
def view_agent_single(request, pk):
    agent = Agent.objects.get(id=pk)
    diction = {'agent': agent}
    return render(request, 'crudapp/view_agent_single.html', context=diction)
