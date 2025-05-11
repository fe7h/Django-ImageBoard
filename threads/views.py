from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView
from rest_framework import viewsets

from .models import Thread
from .forms import AddThreadForm
from .serializers import ThreadSerializers


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


class ParentIDMixin:
    parent_field = ''
    model = None

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.filter(**self._get_filter_key())
        return queryset

    def _get_filter_key(self):
        parent_id = self.kwargs.get(self.parent_field)
        print(parent_id)
        return {self.parent_field.replace('_','__'): parent_id}


class ThreadApiView(ParentIDMixin, viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializers

    model = Thread
    parent_field = 'board_slug'
