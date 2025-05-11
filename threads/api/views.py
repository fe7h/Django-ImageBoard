from rest_framework import viewsets

from threads.models import Thread
from .serializers import ThreadSerializers


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
