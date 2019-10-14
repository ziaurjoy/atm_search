from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView,UpdateView,DeleteView

from buses.models import BusCompany

#class views

class BusCompanisList(ListView):
    model = BusCompany
    context_object_name = 'buses'
    template_name = 'buses/home.html'


class BusCompanisCreate(CreateView):
    model = BusCompany
    template_name = 'buses/create.html'
    fields = '__all__'
    success_url = '/'

class BusCompanisUpadte(UpdateView):
    model = BusCompany
    template_name = 'buses/update.html'
    fields = '__all__'
    success_url = '/'

class BusCompanisDelete(DeleteView):
    model = BusCompany
    template_name = 'buses/delete.html'
    success_url = '/'
