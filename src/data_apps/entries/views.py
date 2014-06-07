from django.shortcuts import render
from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from entries.forms import LoginForm, ProjectForm

from entries.models import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            gebruikersnaam = cd['gebruikersnaam']
            wachtwoord = cd['wachtwoord']
            user = authenticate(username=gebruikersnaam, password=wachtwoord)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                form = LoginForm(request.POST)
                return render_to_response('inloggen.html', {'form': form}, context_instance=RequestContext(request))
        else:
            form = LoginForm(request.POST)
            return render_to_response('inloggen.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        return render_to_response('inloggen.html', {'form': form}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
    
@login_required
def home(request):
    user = request.user
    projects = Project.objects.all()
    return render_to_response("homepage.html", {'user': user, 'projects': projects} , context_instance=RequestContext(request))

@login_required
def project(request, id=None):
    if id:
        #in editmode
        return HttpResponse('Gelukt, het ID is: ' + str(id))
    else:
        #in add mode
        if request.method == 'POST':
            projectform = ProjectForm(request.POST)
            if projectform.is_valid():
                projectform.save(commit=True)
                return HttpResponseRedirect('/')
                #titel = form.cleaned_data['titel']
                #beschrijving = form.cleaned_data['beschrijving']
                #deadline = form.cleaned_data['deadline']
                #sprint = form.cleaned_data['sprint']
            else:
                projectform = ProjectForm(request.POST)
                return render_to_response("formpage.html", {'user': request.user, 'form': projectform} , context_instance=RequestContext(request))

        else:
            projectform = ProjectForm()
            return render_to_response("formpage.html", {'user': request.user, 'form': projectform} , context_instance=RequestContext(request))
