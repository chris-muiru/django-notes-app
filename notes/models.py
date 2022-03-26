from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from authenticate.models import Customer

class Note(models.Model):
    topic = models.CharField(max_length=30)
    Notes = models.TextField()
    date_created = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.topic}'


class Subject(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'

# Create your models her
