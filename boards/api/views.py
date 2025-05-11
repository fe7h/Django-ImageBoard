from rest_framework import viewsets

from boards.models import Board
from boards.serializers import BoardSerializers


class BoardApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers
