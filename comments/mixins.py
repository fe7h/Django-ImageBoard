from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .models import Comment


class CommentedMixin(models.Model):
    comments = GenericRelation(Comment)
