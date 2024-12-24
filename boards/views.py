from django.shortcuts import render, redirect, get_object_or_404

from .models import Board


def board_show(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)

    return render(request, 'boards/board.html', context={'board': board})
