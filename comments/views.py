from django.shortcuts import render, resolve_url, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import AddCommentForm
from .models import Comment


@require_POST
def add_comment(request):

    data = request.POST.copy()
    print(data)
    form = AddCommentForm(data)

    if form.is_valid():
        print(form.cleaned_data)
        com_obj = form.save()

        # next = form.cleaned_data.get('next')
        # url = resolve_url(next)
        # if next == 'about_comment':
        #     response = reverse(next, kwargs={'comment_id': com_obj.pk})
        # else:
        #     response = reverse()
        # return redirect(url)
        return HttpResponse('Done')

    return HttpResponse('Don\'t done')
