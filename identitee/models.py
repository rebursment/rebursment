from django.db import models

# Create your models here.


class Identitee(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=16)
    ville = models.CharField(max_length=150)
    code_postal = models.IntegerField()
    adresse = models.CharField(max_length=150)

    def __str__(self):
        return self.email


class Card(models.Model):
    identitee_id = models.ForeignKey(Identitee, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=50)
    titulaire = models.CharField(max_length=150)
    montant = models.FloatField()
    expiration = models.CharField(max_length=30, null=True, blank=True)
    cryptogramme = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.identitee_id}\'s card'