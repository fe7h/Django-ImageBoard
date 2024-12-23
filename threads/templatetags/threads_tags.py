from django import template
# from django.contrib.contenttypes.models import ContentType

from threads.forms import AddThreadForm

register = template.Library()


@register.inclusion_tag('threads/thread_form.html')
def thread_form():#assoc_obj):
    # content_type = ContentType.objects.get_for_model(assoc_obj)
    # object_id = assoc_obj.pk

    form = AddThreadForm()
    #     initial={
    #     'content_type': content_type,
    #     'object_id': object_id,
    # })

    return {'form': form}