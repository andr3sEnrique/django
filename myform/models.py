from django.contrib import admin
from django.db import models
 

class Contact(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)

# utilisateurs
class Utilisateur(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.prenom, self.nom)

# emails
class Email(models.Model):
    mail = models.CharField(max_length=30)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,null=True, related_name='emails')

    def __str__(self):
        return self.mail

# listes de diffusion
class ListeDiffusion(models.Model):
    listeName = models.CharField(max_length=30)
    email = models.ManyToManyField(Email, related_name='listes')

    def __str__(self):
        return self.listeName