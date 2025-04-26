from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

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


class AddThreadView(CreateView):
    form_class = AddThreadForm

    def get_initial(self):
        initail = super().get_initial()
        initail['board'] = self.kwargs.get('board_slug')
        return initail

    def form_invalid(self, form):
        return HttpResponse('Form don\'t valid!')
