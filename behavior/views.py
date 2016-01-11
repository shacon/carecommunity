from django.shortcuts import render
from .forms import AddBehavior


def addbehavior(request):
    if request.method == 'POST':
        form = AddBehavior(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            antecedent = form.cleaned_data['antecedent']
            consequence = form.cleaned_data['consequence']
            is_positive = form.cleaned_data['is_positive']
            Behavior.objects.publish(description, antecedent, consequence, is_positive)
        else:
            return render(request, 'behavior/addbehavior.html', {'form': form, 'errors': "Something went wrong"})
    else:
        form = AddBehavior()
        return render(request, 'behavior/addbehavior.html', {'form': form})

