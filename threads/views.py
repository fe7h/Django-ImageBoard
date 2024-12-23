from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Thread
from .forms import AddThreadForm


def thread_show(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)

    return render(request,'threads/thread.html', context={'thread' : thread})


@require_POST
def add_thread(request):
    form = AddThreadForm(request.POST, request.FILES)

    if form.is_valid():
        thread_obj = form.save()
        url = resolve_url(thread_obj)
        return redirect(url)

    return HttpResponse('Form don\'t valid!')
