from django.shortcuts import resolve_url, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .forms import AddCommentForm


@require_POST
def add_comment(request):

    data = request.POST.copy()
    print(data)
    form = AddCommentForm(data)

    if form.is_valid():
        print(form.cleaned_data)
        com_obj = form.save()

        next = form.cleaned_data.get('next')
        if next:
            url = resolve_url(next)
            print(url)
            return redirect(url)

        return HttpResponse(com_obj.pk)

    return HttpResponse('Form don\'t valid!')
