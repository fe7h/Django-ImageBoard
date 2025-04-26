from django import template

from threads.forms import AddThreadForm

register = template.Library()


@register.inclusion_tag('threads/thread_preview_list.html')
def thread_preview_list(board_obj):
    threads = board_obj.threads.all()
    return {'threads': threads}


@register.inclusion_tag('threads/thread_form.html')
def thread_form(board_obj):
    board_slug = board_obj.slug

    form = AddThreadForm()

    return {'form': form, 'board_slug': board_slug}
