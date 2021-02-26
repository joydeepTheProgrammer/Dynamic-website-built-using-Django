from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=500)
    city  = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField(max_length=5)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


