from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.shortcuts import render
import json
from django.urls import reverse
from .forms import AddIncidentForm
from .models import *


# Create your views here.
class IncidentsView(ListView):
    model = Incidents
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IncidentsView, self).get_context_data(**kwargs)
        context['data'] = json.dumps(list(Incidents.objects.values('latitude', 'longitude', 'address', 'description', 'taken_measures').all()))
        return context


class IncidentDatail(DetailView):
    model = Incidents
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IncidentDatail, self).get_context_data(**kwargs)
        context['data'] = json.dumps(list(Incidents.objects.filter(pk=kwargs['object'].id).values('latitude', 'longitude','address', 'description', 'taken_measures')))
        return context


class IncidentsAdd(CreateView):
    # model = Incidents
    form_class = AddIncidentForm
    template_name = "Incidents/incidents_form.html"
    success_url = 'incident-detail'

    def get_success_url(self):
        return reverse('incident-detail', kwargs={'pk': self.object.pk})

class IncidentsDelete(DeleteView):
    model = Incidents
    success_url = '/'

class IncidentsUpdate(UpdateView):
    model = Incidents
    form_class = AddIncidentForm
    template_name = "Incidents/incidents_update_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IncidentsUpdate, self).get_context_data(**kwargs)
        context['data'] = json.dumps(list(Incidents.objects.filter(pk=context['object'].id).values('latitude', 'longitude','address', 'description', 'taken_measures')))
        return context

    def get_success_url(self):
        return reverse_lazy('incident-detail', kwargs={'pk': self.object.pk})