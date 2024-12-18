from django.db import models
from comments.mixins import CommentedMixin


class Thread(CommentedMixin):
    title = models.CharField(max_length=100)
    title_img = models.ImageField(upload_to='threads/images/')
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
