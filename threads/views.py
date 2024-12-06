from django.shortcuts import render
from .models import Message

# Create your views here.
def thread(request):
    data = Message.objects.all()
    return render(request,'threads/thread.html', context={'data' : data})