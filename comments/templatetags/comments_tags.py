from django import template
from django.contrib.contenttypes.models import ContentType

from comments.forms import AddCommentForm, AttachedImageForm

register = template.Library()


@register.inclusion_tag('comments/comment_list.html')
def comment_list(assoc_obj):
    comments = assoc_obj.comments.all().prefetch_related('images')
    return {'comments': comments}


@register.inclusion_tag('comments/comment_form.html')
def comment_form(assoc_obj, next=False):
    content_type = ContentType.objects.get_for_model(assoc_obj)
    object_id = assoc_obj.pk

    main_form = AddCommentForm(initial={
        'content_type': content_type,
        'object_id': object_id,
    })
    if next:
        main_form.initial['next'] = next

    image_form = AttachedImageForm()

    return {'main_form': main_form, 'image_form': image_form}
