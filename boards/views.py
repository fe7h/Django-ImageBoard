from django.shortcuts import render, redirect
from .models import ThreadModel


def board(request):
    return render(request, 'boards/board.html')


def temp_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = request.POST.get('data')
        title_img = request.FILES.get('title_img')
        print(title, data, title_img)
        ThreadModel.objects.create(title=title, data=data, title_img=title_img)
        return redirect(temp_form)
    return render(request, 'boards/temp_form.html')