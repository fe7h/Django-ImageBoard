from django.db import models

# Create your models here.
class Message(models.Model):
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='threads/images/')
