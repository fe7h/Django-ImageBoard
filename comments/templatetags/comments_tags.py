from django import template
from django.contrib.contenttypes.models import ContentType

from comments.forms import AddCommentForm

register = template.Library()


@register.inclusion_tag('comments/comment_list.html')
def comment_list(assoc_obj):
    comments = assoc_obj.comments.all()
    return {'comments': comments}


@register.inclusion_tag('comments/comment_form.html')
def comment_form(assoc_obj, next=False):
    content_type = ContentType.objects.get_for_model(assoc_obj)
    object_id = assoc_obj.pk

    form = AddCommentForm(initial={
        'content_type': content_type,
        'object_id': object_id,
    })
    if next:
        form.initial['next'] = next

    return {'form': form}
