from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comment(models.Model):
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class AttachedImage(models.Model):
    message = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name='images')
    img = models.ImageField(upload_to='threads/images/')
