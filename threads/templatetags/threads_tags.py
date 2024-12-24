from django import template
# from django.contrib.contenttypes.models import ContentType

from threads.forms import AddThreadForm
from threads.models import Thread

register = template.Library()


@register.inclusion_tag('threads/thread_preview_list.html')
def thread_preview_list(board_obj):
    threads = board_obj.threads.all()
    return {'threads': threads}


@register.inclusion_tag('threads/thread_form.html')
def thread_form(board_obj):
    board_slug = board_obj.slug
    board_id = board_obj.pk

    form = AddThreadForm(
        initial={
        'board_id': board_id,
    })

    return {'form': form, 'board_slug': board_slug}