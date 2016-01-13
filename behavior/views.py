from django.shortcuts import render
from .forms import AddBehavior
from .models import Behavior
from django.utils import timezone
from caretaker.models import Caregiver

def add_pos_behavior(request):
    caregiver_id = request.user.id
    if request.method == 'POST':
        form = AddBehavior(request.POST)
        if form.is_valid():
            positive_value = True
            description = form.cleaned_data['description']
            antecedent = form.cleaned_data['antecedent_text']
            consequence = form.cleaned_data['consequence_text']
            user = Caregiver.objects.get(pk=caregiver_id)
            behavior = Behavior(client=user, description=description, antecedent_text=antecedent, consequence_text=consequence, is_positive=positive_value)
            behavior.publish()
            return render(request, 'profiles/profiles_list.html', {})
        else:
            return render(request, 'behavior/addbehavior.html', {'form': form, 'errors': "Something went wrong"})
    else:
        form = AddBehavior()
        return render(request, 'behavior/addbehavior.html', {'form': form})

def add_neg_behavior(request):
    if request.method == 'POST':
        form = AddBehavior(request.POST)
        if form.is_valid():
            positive_value = False
            description = form.cleaned_data['description']
            antecedent = form.cleaned_data['antecedent_text']
            consequence = form.cleaned_data['consequence_text']
            Behavior.objects.publish(description, antecedent, consequence, is_positive=positive_value)
            return render(request, 'profiles/profiles_list.html', {})
        else:
            return render(request, 'behavior/addbehavior.html', {'form': form, 'errors': "Something went wrong"})
    else:
        form = AddBehavior()
        return render(request, 'behavior/addbehavior.html', {'form': form})


