from datetime import datetime
from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default='example@email.com')

    # Create your models here.
class Hobbies(models.Model):
    username = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=250)

class Marks(models.Model):
    username = models.CharField(max_length=30)
    marks = models.CharField(max_length=250)

class Todo(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
        