from django.shortcuts import render, redirect
from .models import Thread

# Create your views here.
def thread(request, thread_id):

    threa = Thread.objects.get(pk=thread_id)

    return render(request,'threads/thread.html', context={'thread' : threa})