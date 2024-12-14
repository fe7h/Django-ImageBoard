from django.shortcuts import render, redirect
from .models import Message, Image
from boards.models import ThreadModel

# Create your views here.
def thread(request, thread_id):
    thread_id = ThreadModel.objects.get(pk=thread_id)
    if request.method == 'POST':
        if request.POST['test']:
            print(request.POST)
            msg = Message.objects.create(data=request.POST['test'], thread=thread_id)
            if request.FILES:
                print(request.FILES)
                for file in request.FILES.getlist('img'):
                    print(type(file))
                    Image.objects.create(message=msg, img=file)
        return redirect('thread', thread_id=thread_id.pk)
    data = thread_id.messages.all()
    thread_title = thread_id
    return render(request,'threads/thread.html', context={'data' : data, 'thread_title' : thread_title})