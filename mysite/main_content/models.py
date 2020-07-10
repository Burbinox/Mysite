from django.db import models


class Praca(models.Model):
    zdjecie = models.ImageField(upload_to='media')
    nazwa = models.CharField(max_length=250)
    czas_pracy = models.CharField(max_length=250)
    opis = models.TextField()


class Skills(models.Model):
    zdjecie = models.ImageField(upload_to='media')
    nazwa = models.CharField(max_length=250)
    dosw_prywatne = models.CharField(max_length=250)
    dosw_zawodowe = models.CharField(max_length=250)
    opis = models.TextField()


class Hobby(models.Model):
    zdjecie = models.ImageField(upload_to='media')
    nazwa = models.CharField(max_length=250)
    opis = models.TextField()
