from django.shortcuts import render, render_to_response
from .models import Client
from caretaker.models import Caregiver
from behavior.models import Behavior
from django.contrib.auth import authenticate
from django.template import RequestContext

def profiles_list(request):
    context = RequestContext(request)
    user = request.user
    client_list = [client for client in Client.objects.all() if client.caregiver == user]
    context_dict = {'client':client_list}
    if user.is_authenticated() and user == Caregiver.objects.get(id=user.id):
	return render_to_response('profiles/profiles_list.html', context_dict, context)
    else:
    #add message to user must sign in order to view profile
	return render(request, 'registration/login.html', {})

def individual_profile(request, client_id):
    context = RequestContext(request)
    client = Client.objects.get(nickname=client_id)
    pos_behaviors = Behavior.objects.filter(client=client, is_positive=True)
    neg_behaviors = Behavior.objects.filter(client=client, is_positive=False)
    context_dict = {'client':client, 'neg_behaviors':neg_behaviors, 'pos_behaviors':pos_behaviors}
    return render_to_response('profiles/individual_profile.html', context_dict, context)

def search(request):
    return render(request, 'profiles/search.html', {})

