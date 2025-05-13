from django import forms

from utils.utils import get_related_model_by_field_name, NoRenderFieldsMixin

from .models import Thread


class AddThreadForm(NoRenderFieldsMixin, forms.ModelForm):
    no_render_fields = ('board',)

    board = forms.Field()

    class Meta:
        model = Thread
        fields = ['title', 'title_img', 'data', 'board']

    def clean_board(self):
        related_model = get_related_model_by_field_name(self._meta.model, 'board')
        slug = self.cleaned_data.get('board')
        return related_model.objects.only('slug').get(slug=slug)
