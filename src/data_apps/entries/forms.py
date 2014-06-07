from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from entries.models import Project

class LoginForm(forms.Form):
    gebruikersnaam = forms.CharField(label='Gebruikersnaam')
    wachtwoord = forms.CharField(widget=forms.PasswordInput(), label='Wachtwoord')

class ProjectForm(forms.ModelForm):
    deadline = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Project
        #fields = ['titel', 'beschrijving', 'deadline', 'sprint']
