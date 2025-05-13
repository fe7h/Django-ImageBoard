from django.apps import apps
from django.db import models


def get_related_model_by_field_name(model: models.Model, field_name: str):
    """Return class of related model.

    Args:
        model (models.Model): Model class with related field
        field_name (str): Name of related field

    Returns:
        model.Model: Class of related model
    """
    related_model_name = model._meta.get_field(field_name).related_model._meta.label
    related_model = apps.get_model(related_model_name)
    return related_model


class NoRenderFieldsMixin:
    """Mixin for Forms. Allows creating form fields that are processed but not rendered in HTML.

    Must to use together with initial data, like Form(initial={'no_render_fields[0]': value, ...}).

    When forms calling the internal clean method,
    Django performs a check: 'bf.initial if field.disabled else bf.data'.
    This class made all field in no_render_fields disabled and delete this fields from render
    by overriding the get_context method.

    Attributes:
        no_render_fields (tuple): Fields that will not be rendered
    """

    no_render_fields = ()

    def __init__(self, *args, **kwargs):
        """Disabled all fields in no_render_fields"""
        super().__init__(*args, **kwargs)
        for field in self.no_render_fields:
            self.fields.get(field).disabled = True

    @staticmethod
    def _redesign(data, bad):
        """Pop no_render_fields from context list

        Args:
            data: [(django.forms.boundfield.BoundField, ...), ...]
            bad: no_render_fields
        """
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


def related_model_manager_factory(related_field_name: str) -> models.Manager:
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().select_related(related_field_name)
    return NewManager()
