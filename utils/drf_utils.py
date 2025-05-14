from rest_framework import exceptions

from utils.utils import get_related_model_by_field_name


class ParentIDMixin:
    parent_field = ''
    model = None

    def get_queryset(self, *args, **kwargs):
        filter_key = self._get_filter_key()
        self._parent_obj_exist(*tuple(filter_key.items())[0])
        queryset = self.model.objects.filter(**filter_key)
        return queryset

    def _parent_obj_exist(self, parent_field, parent_id):
        parent_model = get_related_model_by_field_name(self.model, parent_field)
        if not parent_model.objects.filter(pk=parent_id).exists():
            raise exceptions.NotFound()

    def _get_filter_key(self):
        parent_id = self.kwargs.get(self.parent_field)
        return {self.parent_field: parent_id}
