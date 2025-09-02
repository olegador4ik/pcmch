from django.db import models

# Create your models here.

class I(models.Model):
    c = models.CharField(max_length=10)
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

class Q(models.Model):
    n = models.IntegerField()
    rus = models.CharField(max_length=150)
    eng = models.CharField(max_length=150)

class IT(models.Model):
    q = models.ForeignKey(I, on_delete=models.CASCADE, related_name="ia")
    rus = models.CharField(max_length=20)
    eng = models.CharField(max_length=20)