from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
