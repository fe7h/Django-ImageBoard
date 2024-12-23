from django.db import models
from django.urls import reverse

from comments.mixins import CommentedMixin


class Thread(CommentedMixin):
    title = models.CharField(max_length=100)
    title_img = models.ImageField(upload_to='threads/images/')
    data = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('thread', kwargs={'thread_id': self.pk})
