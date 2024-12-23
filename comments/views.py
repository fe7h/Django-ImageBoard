from django.shortcuts import resolve_url, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .forms import AddCommentForm, AttachedImageForm


@require_POST
def add_comment(request):
    post_data = request.POST.copy()
    main_form = AddCommentForm(post_data)
    image_form = AttachedImageForm(post_data, request.FILES)

    if main_form.is_valid():
        comment_pk = main_form.save().pk

        if post_data.get('images') is None and image_form.is_valid():
            image_form.save(comment_pk)

        next = main_form.cleaned_data.get('next')
        if next:
            url = resolve_url(next)
            return redirect(url)

        return HttpResponse(comment_pk)

    return HttpResponse('Form don\'t valid!')
