import string
import random

from django.core.management.base import BaseCommand
from comments.models import Comment
from django.apps import apps


def rand_message():
    sentence = ''
    for i in range(random.randint(6,30)):
        lenth = 12
        while True:
            sentence = sentence + random.choice(string.ascii_lowercase)
            if lenth == 0 or random.randint(1,lenth) == 1:
                break
            lenth -= 1
        sentence += ' '
    return sentence


class Command(BaseCommand):
    help = "Fills db with data"

    def add_arguments(self, parser):
        parser.add_argument('app_model', metavar='app.model', type=str)
        parser.add_argument('pk', type=int)

    def handle(self, *args, **options):
        app_label, model_name = options['app_model'].split('.')
        pk = options['pk']

        model = apps.get_model(app_label=app_label, model_name=model_name)

        model_obj = model.objects.get(pk=pk)

        for i in range(10):
            Comment.objects.create(data=rand_message(), content_object=model_obj)
