from django import forms
from django.core.exceptions import ValidationError
from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from .models import Comment, AttachedImage


class AddCommentForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)

    next = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )

    def clean_content_type(self):
        content_type = self.cleaned_data.get('content_type')
        app_model = content_type.replace(' | ', '.')
        try:
            model = apps.get_model(app_model)
            return ContentType.objects.get_for_model(model)
        except:
            raise ValidationError('Model not found')

    class Meta:
        model = Comment
        fields = ['data', 'content_type', 'object_id']


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class AttachedImageForm(forms.Form):
    images = MultipleImageField(required=False)

    def save(self, comment_pk):
        images = self.cleaned_data.get('images')
        for img in images:
            AttachedImage.objects.create(img=img, comment_id=comment_pk)
