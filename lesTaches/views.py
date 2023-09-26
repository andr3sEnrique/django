from django.shortcuts import render
from django.http import HttpResponse
from lesTaches.models import Task, Email # import de la class Tas
# Create your views here.

def task_listing(request):
    from django.template import Template,Context
    objets=Task.objects.all().order_by('due_date')
    template=Template('{% for elem in objets %} {{elem}} <br />{%endfor%}')
    print(str(template))
    context=Context({'objets':objets})
    print(str(template.render(context)))
    return HttpResponse(template.render(context))

def task_listing2(request):
    objects = Task.objects.all().order_by('due_date')
    return render(request, template_name='list2.html', context={'objects': objects} )

def home(request, name):
    return HttpResponse("Bonjour depuis Django " + name)

#views.py
def email_detail(request, pk):
    email = Email.objects.get(pk=pk)
    user = email.user
    listes_abonnees = email.listes.all()
    template = 'email_detail.html'
    context = {'user': user, 'email': email.mail, 'listes': listes_abonnees }
    return render(request, template, context)