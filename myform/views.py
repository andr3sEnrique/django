from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from myform.models import Contact
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom "
        self.fields['firstname'].label = "Prenom"
        self.fields['email'].label = "mél"
    
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),}

def contact(request):
    # on instancie un formulaire
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            # on prépare un nouveau message
            messages.success(request, 'Nouveau contact ' + new_contact.name + ' ' + new_contact.email)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request, 'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request, 'contact.html', context)

def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    context = {'pers': contact}
    return render(request, 'detail.html', context)
