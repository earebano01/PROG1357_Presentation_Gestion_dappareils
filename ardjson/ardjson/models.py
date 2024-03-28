# from django.contrib import admin
# from django.db import models

# class Actionneur(models.Model):
#     actionneur_id = models.AutoField(primary_key=True)
#     objet = models.ForeignKey('Objetconnecte', models.CASCADE, blank=True, null=True)
#     status = models.CharField(max_length=10, blank=True, null=True)
#     formatted_date = models.CharField(max_length=50, blank=True, null=True)
#     formatted_time = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'actionneur'

# class Capteur(models.Model):
#     capteur_id = models.AutoField(primary_key=True)
#     objet = models.ForeignKey('Objetconnecte', models.CASCADE, blank=True, null=True)
#     status = models.CharField(max_length=10, blank=True, null=True)
#     temperature = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     humidite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     son = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     lumiere = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     formatted_date = models.CharField(max_length=50, blank=True, null=True)
#     formatted_time = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'capteur'

# class Objetconnecte(models.Model):
#     objet_id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=255, blank=True, null=True)
#     device_id = models.CharField(max_length=50, blank=True, null=True)
#     type = models.CharField(max_length=50, blank=True, null=True)
#     typemesure = models.CharField(max_length=50, blank=True, null=True)
#     typeaction = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'objetconnecte'

from django.contrib import admin
from django.db import models

class Actionneur(models.Model):
    actionneur_id = models.AutoField(primary_key=True)
    objet = models.ForeignKey('Objetconnecte', models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    formatted_date = models.CharField(max_length=50, blank=True, null=True)
    formatted_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actionneur'

class Capteur(models.Model):
    capteur_id = models.AutoField(primary_key=True)
    objet = models.ForeignKey('Objetconnecte', models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    humidite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    son = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lumiere = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    formatted_date = models.CharField(max_length=50, blank=True, null=True)
    formatted_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capteur'

class Objetconnecte(models.Model):
    objet_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    typemesure = models.CharField(max_length=50, blank=True, null=True)
    typeaction = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetconnecte'