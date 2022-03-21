from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Note(models.Model):
    topic = models.CharField(max_length=30)
    Notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(default=now)

# Create your models her
