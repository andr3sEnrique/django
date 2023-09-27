from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Morceau

def morceau_detail(request,pk):
        return HttpResponse('OK')

class MorceauDetailView(DetailView):
    model = Morceau

class MorceauList(ListView):
    model = Morceau