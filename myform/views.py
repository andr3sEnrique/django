from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from myform.models import Contact
from .models import Utilisateur, Email, ListeDiffusion
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


# On crée 2 utilisateurs
user1 = Utilisateur(nom='user1')
user2 = Utilisateur(nom='user2')

# On crée les mails associés
email1 = Email(mail='user1@baba.fr', user=user1)
email2 = Email(mail='user2@bibi.fr', user=user2)

# On crée 4 listes de diffusion
liste1 = ListeDiffusion(listeName='liste1')
liste2 = ListeDiffusion(listeName='liste2')
liste3 = ListeDiffusion(listeName='liste3')
liste4 = ListeDiffusion(listeName='liste4')

# on sauvegarde tout le monde
user1.save()
user2.save()
email1.save()
email2.save()
liste1.save()
liste2.save()
liste3.save()
liste4.save()

# on ajoute les emails à des listes
liste1.email.add(email1)
liste1.email.add(email2)
liste2.email.add(email1)
liste3.email.add(email1)
liste3.email.add(email2)
liste4.email.add(email2)

# Pour obtenir toutes les listes auxquelles l'email1 est abonné :
email1.listes.all()
# Et celles auxquelles l'email2 est abonné :
email2.listes.all()

#views.py
def email_detail(request, pk):
    email = Email.objects.get(pk=pk)
    user = email.user
    listes_abonnees = email.listes.all()
    template = 'email_detail.html'
    context = {'user': user, 'email': email.mail, 'listes': listes_abonnees }
    return render(request, template, context)