from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Board


class BoardDetailView(DetailView):
    model = Board
    template_name = 'boards/board.html'
    context_object_name = 'board'
    slug_url_kwarg = 'board_slug'
