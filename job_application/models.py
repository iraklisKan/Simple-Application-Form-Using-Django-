
from django.db import models

class Form(models.Model):
    first_Name=models.CharField(max_length=100)
    last_Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"