from django.db import models

from boards.models import ThreadModel

# Create your models here.
class Message(models.Model):
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='messages')


class Image(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='threads/images/')
