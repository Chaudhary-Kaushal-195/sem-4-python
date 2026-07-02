from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField()
    test = models.IntegerField()
    runs = models.IntegerField()
    
    def __str__(self):
        return f"{self.runs} - {self.name}"