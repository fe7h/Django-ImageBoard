from django.db import models
from django.urls import reverse

from comments.mixins import CommentedMixin


def related_model_manager_factory(related_field_name:str) -> models.Manager:
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().select_related(related_field_name)
    return NewManager()


class Thread(CommentedMixin):
    title = models.CharField(max_length=100)
    title_img = models.ImageField(upload_to='threads/images/', blank=True, null=True)
    data = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE, related_name='threads')

    with_related_board = related_model_manager_factory('board')

    def get_absolute_url(self):
        return reverse('thread', kwargs={'thread_id': self.pk, 'board_slug': self.board.slug})
