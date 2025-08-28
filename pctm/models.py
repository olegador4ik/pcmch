from django.db import models

# Create your models here.
class Q(models.Model):
    q = models.CharField(max_length=150)
    n = models.IntegerField()

    def __str__(self):
        return self.q

class I(models.Model):
    n = models.CharField(max_length=20)
    c = models.CharField(max_length=10)
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

    def __str__(self):
        return self.n