from django.shortcuts import render, render_to_response
from .models import Client
from caretaker.models import Caregiver
from behavior.models import Behavior
from django.contrib.auth import authenticate
from django.template import RequestContext
from .forms import AddClient

def profiles_list(request):
    user = request.user
    client_list = user.client_set.all()
    context = {'client': client_list}
    if user.is_authenticated():
        return render(request, 'profiles/profiles_list.html', context)
    else:
    #add message to user must sign in order to view profile
        return render(request, 'registration/login.html', {})

def individual_profile(request, client_id):
    client = Client.objects.get(id=client_id)
    pos_behaviors = Behavior.objects.filter(client=client, is_positive=True)
    neg_behaviors = Behavior.objects.filter(client=client, is_positive=False)
    context = {'client': client, 'neg_behaviors': neg_behaviors, 'pos_behaviors': pos_behaviors}
    return render(request, 'profiles/individual_profile.html', context)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        behaviors = Behavior.objects.filter(description__icontains=q)
        return render(request, 'profiles/search.html',
            {'behaviors': behaviors, 'query': q})
    else:
        return render(request, 'profiles/search.html')


def addclient(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        user = request.user
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            Client.objects.create(caregiver=user, nickname=nickname)
            user = request.user
            client_list = user.client_set.all()
            context = {'client': client_list}
            return render(request, 'profiles/profiles_list.html', context)
        else:
            return render(request, 'profiles/addclient.html', {'form': form, 'errors': "Something went wrong"})
    else:
        form = AddClient()
        return render(request, 'profiles/addclient.html', {'form': form})










