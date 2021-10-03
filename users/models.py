from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Couses(models.Model):
    subject = models.CharField(max_length=64)
    term = models.IntegerField()
    couseid = models.IntegerField()
    num_student = models.IntegerField()
    year = models.IntegerField()
    nisit = models.ManyToManyField(User, blank=True,name="nisit")
    status = models.BooleanField(default=True)

    
    def __str__(self):
        return f"{self.id}:Subject {self.subject} | Couses ID {self.couseid} "

