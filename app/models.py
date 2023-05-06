from django.db import models
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='images/')
    Desc=models.TextField()
def _str_(self):
     return self.name

# Create your models here.
