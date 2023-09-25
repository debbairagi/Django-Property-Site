from django.shortcuts import render, redirect
from userapp.forms import CreateUserForm, LoginForm, CreateAgentForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

# - Register A User
def userapp_register(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            # messages.success(request, 'Account created successfully!')
            return redirect('userapp_login')

    diction = {'register_form': register_form}
    return render(request, 'userapp/register-page.html', context=diction)


# Login A User
def userapp_login(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request, data = request.POST)

        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                # messages.success(request, 'You have logged!')
                return redirect('dashboard')

    diction = {'login_form': login_form}
    return render(request, 'userapp/login-page.html', context=diction)

@login_required(login_url='userapp_login')
def userapp_logout(request):
    auth.logout(request)
    return redirect('index')


def userapp_agent_form(request):

    agent_form = CreateAgentForm()

    if request.method == 'POST':
        agent_form = CreateAgentForm(request.POST)
        if agent_form.is_valid():
            agent_form.save()
            return redirect('index')
    diction = {'agent_form':agent_form}
    return render(request, 'userapp/create-agent.html', context=diction)
