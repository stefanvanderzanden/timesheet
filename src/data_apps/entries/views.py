from django.shortcuts import render
from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from entries.forms import LoginForm, ProjectForm, DeelTaakForm, TijdBestedingForm

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
    projects = []
    for project in Project.objects.all():
        verwacht = 0.0
        besteed = 0.0
        for deeltaak in DeelTaak.objects.filter(project=project):
            verwacht += deeltaak.verwachte_tijd
        for tijdentry in TijdEntry.objects.filter(deeltaak__project=project):
            besteed += tijdentry.tijdbesteding

        try:
            percentage = round((besteed/verwacht)*100,2)
        except:
            percentage = 0.0
            
        projects.append({'id': project.id,
                         'titel': project.titel,
                         'deadline': project.deadline,
                         'beschrijving': project.beschrijving,
                         'sprint': project.sprint,
                         'verwacht': verwacht,
                         'besteed': besteed,
                         'percentage': percentage})
    return render_to_response("homepage.html", {'user': user, 'projects': projects} , context_instance=RequestContext(request))

@login_required
def form(request, onderdeel, id=None):
    mode = 'bewerken' if id else 'toevoegen'
    if onderdeel == 'project':
        page = 'form-project.html'
        form = {}
        form['leeg'] = ProjectForm()
        form['request'] = ProjectForm(request.POST)
        if id:
            project=Project.objects.get(pk=id)
            form['instance'] = ProjectForm(instance=project)
            form['request_instance'] = ProjectForm(request.POST, instance=project)
    elif onderdeel == 'deeltaak':
        page = 'form-deeltaak.html'
        form = {}
        form['leeg'] = DeelTaakForm()
        form['request'] = DeelTaakForm(request.POST)
        if id:
            deeltaak=DeelTaak.objects.get(pk=id)
            form['instance'] = DeelTaakForm(instance=deeltaak)
            form['request_instance'] = DeelTaakForm(request.POST, instance=deeltaak)
    elif onderdeel == 'tijdbesteding':
        page = 'form-tijdbesteding.html'
        form = {}
        form['leeg'] = TijdBestedingForm()
        form['request'] = TijdBestedingForm(request.POST)
        if id:
            tijdbesteding=TijdEntry.objects.get(pk=id)
            form['instance'] = TijdBestedingForm(instance=tijdbesteding)
            form['request_instance'] = TijdBestedingForm(request.POST, instance=tijdbesteding)
        
        
    if id:
    #in editmode
        if request.method == 'POST':
            if form['request_instance'].is_valid():
                form['request_instance'].save(commit=True)
                return HttpResponseRedirect('/')
            else:
                return render_to_response(page, {'user': request.user, 'form': form['request'], 'mode': mode}, context_instance=RequestContext(request))
        else:
            return render_to_response(page, {'user': request.user, 'form': form['instance'], 'mode': mode}, context_instance=RequestContext(request))

    else:
        #in add mode
        if request.method == 'POST':
            projectform = ProjectForm(request.POST)
            if form['request'].is_valid():
                form['request'].save(commit=True)
                return HttpResponseRedirect('/')
            else:
                return render_to_response(page, {'user': request.user, 'form': form['request'], 'mode': mode}, context_instance=RequestContext(request))

        else:
            return render_to_response(page, {'user': request.user, 'form': form['leeg'], 'mode': mode}, context_instance=RequestContext(request))
            
