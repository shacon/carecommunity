from django import forms
from .models import Behavior, Client


class AddBehavior(forms.ModelForm):

    class Meta:
    	model = Behavior
    	fields = ('description','antecedent_text','consequence_text', 'is_positive' )


