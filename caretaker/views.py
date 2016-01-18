from django.shortcuts import render
from .forms import Signup, Login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Caregiver
from profiles.models import Client


def index(request):
    return render(request, 'caretaker/index.html', {})

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            Caregiver.objects.create_user(email, password, form.cleaned_data['first_name'], form.cleaned_data['last_name'])
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return render(request, 'registration/thanks.html', {})
        else:
            return render(request, 'registration/signup.html', {'form': form, 'errors': "Something went wrong"})
    else:
        form = Signup()
        return render(request, 'registration/signup.html', {'form': form})

def login(request):
    form = Login()
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'registration/login.html', {'form': form, 'errors': "Your account appears to be inactive"})
        else:
            return render(request, 'registration/login.html', {'form': form, 'errors': "Looks like you haven't signed up yet."})
    else:
        return render(request, 'registration/login.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            auth_logout(request)
            return HttpResponseRedirect('registration/logout_success.html')
        else:
            return HttpResponseRedirect('caretaker/index.html', {})
    else:
        return render(request, 'registration/logout.html', {})

def thanks(request):
    return render(request, 'registration/thanks.html', {})

def about(request):
    return render(request, 'caretaker/about.html', {})

def demo(request):
    return render(request, 'caretaker/demo.html', {})


