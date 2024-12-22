from email.policy import default

from django import forms
from django.core.exceptions import ValidationError
from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from .models import Comment, AttachedImage


class AddCommentForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)

    # next = forms.CharField(widget=forms.HiddenInput, default='about_comment')

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
