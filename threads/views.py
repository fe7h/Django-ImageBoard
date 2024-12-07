from django.shortcuts import render
from .models import Message

# Create your views here.
def thread(request):
    if request.method == 'POST':
        if request.POST['test']:
            print(request.POST['test'])
            Message.objects.create(data=request.POST['test'])
    data = Message.objects.all()
    return render(request,'threads/thread.html', context={'data' : data})