from django import template


register = template.Library()


@register.inclusion_tag('comments/comment_list.html')
def comments_list(assoc_obj):
    comments = assoc_obj.comments.all()
    return {'comments': comments}
