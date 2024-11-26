import string
import random


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



if __name__ != '__main__':

    from django.core.management.base import BaseCommand, CommandError
    from threads.models import Message


    class Command(BaseCommand):
        help = "Fills db with data"

        # def add_arguments(self, parser):
        #     parser.add_argument()

        def handle(self, *args, **options):
            for i in range(10):
                Message.objects.create(data=rand_message())



if __name__ == '__main__':
    print(rand_message())
