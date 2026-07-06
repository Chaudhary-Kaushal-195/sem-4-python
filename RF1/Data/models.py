from django.db import models

# Create your models here.
class Fac(models.Model):
    name = models.CharField()
    subject = models.CharField()
    score = models.IntegerField()
    grade = models.CharField()
    pr_grade = models.CharField()
    
    def __str__(self):
        return self.name