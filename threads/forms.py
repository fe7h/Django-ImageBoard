from django import forms
from django.apps import apps

from .models import Thread


class NoRenderFieldsMixin:
    '''Использовать вместе с Form(initial={'no_render_fields[0]': value, ...}

    При вызове внутренего клин метода джанго делает проверку:
    bf.initial if field.disabled else bf.data
    '''
    no_render_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.no_render_fields:
            self.fields.get(field).disabled = True

    @staticmethod
    def _redesign(data, bad):
        '''data: [(django.forms.boundfield.BoundField, ...), ...]
        '''
        to_remove = []
        for i in range(len(data)):
            if data[i][0].name in bad:
                to_remove.append(i)
        for i in to_remove:
            data.pop(i)

    def get_context(self):
        context = super().get_context()
        fields = context['fields']
        self._redesign(fields, self.no_render_fields)
        return context


class AddThreadForm(NoRenderFieldsMixin, forms.ModelForm):
    no_render_fields = ('board',)

    board = forms.Field()

    class Meta:
        model = Thread
        fields = ['title', 'title_img', 'data', 'board']

    def clean_board(self):
        related_model_name = self._meta.model._meta.get_field('board').related_model._meta.label
        related_model = apps.get_model(related_model_name)
        slug = self.cleaned_data.get('board')
        return related_model.objects.only('slug').get(slug=slug)
