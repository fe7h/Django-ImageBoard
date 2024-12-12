from django.shortcuts import render, redirect
from .models import Message, Image

# Create your views here.
def thread(request):
    if request.method == 'POST':
        if request.POST['test']:
            print(request.POST)
            msg = Message.objects.create(data=request.POST['test'])
            if request.FILES:
                print(request.FILES)
                for file in request.FILES.getlist('img'):
                    print(type(file))
                    Image.objects.create(message=msg, img=file)
        return redirect(thread)
    data = Message.objects.all()
    return render(request,'threads/thread.html', context={'data' : data})