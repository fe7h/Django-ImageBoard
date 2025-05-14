from rest_framework.decorators import action
from rest_framework import mixins

from comments.api.serializers import WriteCommentSerializers


class _CreateComment(mixins.CreateModelMixin):
    """Uses CreateModelMixin methods to save obj and generate a response."""
    content_object = None

    serializer_class = WriteCommentSerializers

    def set_content_object(self, obj):
        self.content_object = obj

    def perform_create(self, serializer):
        serializer.save(content_object=self.content_object)

    def get_serializer(self, *args, **kwargs):
        """Does not create 'context' unlike the analogous method in GenericAPIView."""
        return self.serializer_class(*args, **kwargs)


class CommentApiMixin:
    """The mixin for GenericAPIView implements an endpoint for adding comments."""
    _create_comment = _CreateComment()

    def get_commentated_object(self, **kwargs):
        return self.get_object()

    @action(detail=True, methods=('post',))
    def comment(self, request, **kwargs):
        commentated_object = self.get_commentated_object(request=request, **kwargs)
        self._create_comment.set_content_object(commentated_object)
        return self._create_comment.create(request)
