from django.db import models

# Create your models here.
class Course(models.Model):
    course = models.CharField()
    duration = models.IntegerField()
    
def __str__(self):
    return self.name
    
class Student(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE, related_name = 'students')
    name = models.CharField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name