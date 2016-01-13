from django import forms
from behavior.models import Client


class AddClient(forms.ModelForm):

    class Meta:
    	model = Client
    	fields = ('nickname',)


