from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Thread
from .forms import AddThreadForm


def thread_show(request, board_slug, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    return render(request,'threads/thread.html', context={'thread' : thread})


@require_POST
def add_thread(request, board_slug):
    form = AddThreadForm(request.POST, request.FILES)

    print(request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        thread_obj = form.save(commit=False)
        thread_obj.board_id = form.cleaned_data.get('board_id')
        thread_obj.save()
        url = resolve_url(thread_obj)
        return redirect(url)

    return HttpResponse('Form don\'t valid!')
