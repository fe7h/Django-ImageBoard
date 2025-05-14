from rest_framework import serializers

from threads.models import Thread
from comments.api.serializers import ReadCommentSerializers


class BaseThreadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'


class DetailThreadSerializers(BaseThreadSerializers):
    comments = ReadCommentSerializers(many=True, read_only=True)

    class Meta(BaseThreadSerializers.Meta):
        read_only_fields = '__all__'


class ListThreadSerializers(BaseThreadSerializers):
    pass
