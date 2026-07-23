from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField()
    country = models.CharField()
    bas = models.CharField()
    bos = models.CharField()
    age = models.IntegerField()
    rs = models.IntegerField()
    wt = models.IntegerField()

    def __str__(self):
        return self.name