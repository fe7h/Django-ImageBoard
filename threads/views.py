from django.shortcuts import render, redirect

from .models import Thread


def thread_show(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)

    return render(request,'threads/thread.html', context={'thread' : thread})
