from django.shortcuts import render, render_to_response
from .models import Client
from caretaker.models import Caregiver
from django.contrib.auth import authenticate
from django.template import RequestContext

def profiles_list(request):
    context = RequestContext(request)
    user = request.user
    client_list = [client for client in Client.objects.all() if client.caregiver == user]
    context_dict = {'client':client_list}

    print context
    print context_dict
    if user.is_authenticated() and user == Caregiver.objects.get(id=user.id):
	return render_to_response('profiles/profiles_list.html', context_dict, context)
    else:
	return render(request, 'caretaker/about.html', {})

def individual_profile(request, id):

	return render(request, 'caretaker/about.html', {})



# def profile(request, id):
#     user = request.user
#     #which form should I use here-and should I change forms.py in caretaker? make a form in behavior?
#     #do i need to use a csrf token somewhere in here?
#     if request.method == 'POST':
#         #if user.is_authenticated:
#         return render(request, 'caretaker/about.html', {})
#         #else: reject 403
#     else:
#         #how to check if user is logged in to view this particular profile?
#         if user.is_authenticated: #does this really check if the current user is logged in?
#             return render(request, 'caretaker/about.html', {})


