from django.db import models
from django.urls import reverse


class Board(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('board-show', kwargs={'board_slug': self.slug})
