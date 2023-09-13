from django.shortcuts import render
from django.http import HttpResponse
from lesTaches.models import Task # import de la class Tas
# Create your views here.

def task_listing(request):
    from django.template import Template, Context
    objects=Task.objects.all().order_by('due_date')
    template=Template('{% for elem in objets %} {{elem}} <br />{%endfor%}')
    print(str(template))
    context=Context({'objects':objects})
    print(str(template.render(context)))

def home(request, name):
    return HttpResponse("Bonjour depuis Django " + name)