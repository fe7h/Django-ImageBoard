from django import forms
# from django.core.exceptions import ValidationError
# from django.apps import apps
# from django.contrib.contenttypes.models import ContentType

from .models import Thread


class AddThreadForm(forms.ModelForm):
    board_id = forms.IntegerField(widget=forms.HiddenInput)

    # def clean_content_type(self):
    #     content_type = self.cleaned_data.get('content_type')
    #     app_model = content_type.replace(' | ', '.')
    #     try:
    #         model = apps.get_model(app_model)
    #         return ContentType.objects.get_for_model(model)
    #     except:
    #         raise ValidationError('Model not found')

    class Meta:
        model = Thread
        fields = ['title', 'title_img', 'data', 'board_id'] #, 'content_type', 'object_id']