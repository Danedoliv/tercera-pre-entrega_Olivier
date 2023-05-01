from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Libro(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    date = models.DateField()

class Editorial(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    date = models.DateField()
