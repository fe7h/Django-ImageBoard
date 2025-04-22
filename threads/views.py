from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from .models import Thread
from .forms import AddThreadForm


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'threads/thread.html'
    context_object_name = 'thread'
    slug_url_kwarg = 'board_slug'
    pk_url_kwarg = 'thread_id'

    def get_object(self, queryset=None):
        return get_object_or_404(
            self.model.with_related_board,
            pk=self.kwargs[self.pk_url_kwarg],
            board__slug=self.kwargs[self.slug_url_kwarg],
        )


@require_POST
def add_thread(request, board_slug):
    form = AddThreadForm(request.POST, request.FILES)

    print(request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        thread_obj = form.save()
        url = resolve_url(thread_obj)
        return redirect(url)

    return HttpResponse('Form don\'t valid!')
