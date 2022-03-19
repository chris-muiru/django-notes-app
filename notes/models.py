from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)


class Notes(models.Model):
    topic = models.CharField(max_length=30)
    Notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    subject = models.ForeignKey('Subject', on_delete=CASCADE)


class Subject(models):
    subject = models.CharField(max_length=20)




# Create your models her
