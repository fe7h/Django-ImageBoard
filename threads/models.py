from django.db import models
from django.urls import reverse

from utils.utils import related_model_manager_factory

from comments.mixins import CommentedMixin


class Thread(CommentedMixin):
    title = models.CharField(max_length=100)
    title_img = models.ImageField(upload_to='threads/images/', blank=True, null=True)
    data = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE, related_name='threads')

    with_related_board = related_model_manager_factory('board')

    def get_absolute_url(self):
        return reverse('thread', kwargs={'thread_id': self.pk, 'board_slug': self.board.slug})

    class Meta:
        ordering = ['-time_create']
