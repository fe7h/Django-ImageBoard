from django.shortcuts import render

# Create your views here.
def thread(request):
    return render(request,'threads/thread.html')