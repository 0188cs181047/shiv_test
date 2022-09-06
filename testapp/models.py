from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length = 30)
    esal = models.FloatField()
    eaddre = models.CharField(max_length = 30)

    def __str__(self):
        return self.ename
