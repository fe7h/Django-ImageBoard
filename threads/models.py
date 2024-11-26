from django.db import models

# Create your models here.
class Message(models.Model):
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)