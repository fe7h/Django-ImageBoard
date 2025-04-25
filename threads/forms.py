from django import forms

from .models import Thread


class NoRenderFieldsMixin:
    # переписать по красоте
    no_render_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.no_render_fields:
            self.fields.get(field).disabled = True

    @staticmethod
    def _redesign(data, bad):
        # data: [(django.forms.boundfield.BoundField, ...), ...]
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

    class Meta:
        model = Thread
        fields = ['title', 'title_img', 'data', 'board']

    def save(self, *args, **kwargs):
        thread_obj = super().save(commit=False)
        thread_obj.board_id = self.cleaned_data.get('board_id')
        thread_obj.save()
        return thread_obj


# Thread._meta.get_field('board').related_model._meta.label >>> 'boards.Board'
# model = get_model(app_str, model_str)
# model.get(slug=board_slug)

# value = bf.initial if field.disabled else bf.data
