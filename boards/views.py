from django.views.generic import DetailView, ListView
from rest_framework import viewsets

from .models import Board
from .serializers import BoardSerializers


class BoardDetailView(DetailView):
    model = Board
    template_name = 'boards/board.html'
    context_object_name = 'board'
    slug_url_kwarg = 'board_slug'


class BoardListView(ListView):
    model = Board
    template_name = 'boards/board_list.html'
    context_object_name = 'boards'


class BoardApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers
