from django import forms

from .models import Caregiver



class Signup(forms.ModelForm):

    password = forms.CharField(max_length=64, widget=forms.widgets.PasswordInput)

    class Meta:
        model = Caregiver
        fields = ('email', 'first_name', 'last_name')

class Login(forms.ModelForm):

    password = forms.CharField(max_length=64, widget=forms.widgets.PasswordInput)

    class Meta:
    	model = Caregiver
    	fields = ('email',)

