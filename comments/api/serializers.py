from rest_framework import serializers

from comments.models import Comment, AttachedImage


class AttachedImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttachedImage
        exclude = ('comment',)


class ReadCommentSerializers(serializers.ModelSerializer):
    images = AttachedImageSerializers(many=True)

    class Meta:
        model = Comment
        exclude = ('object_id', 'content_type')
        read_only_fields = ('__all__',)


class WriteCommentSerializers(serializers.ModelSerializer):
    images = AttachedImageSerializers(many=True, required=False)

    class Meta:
        model = Comment
        exclude = ('object_id', 'content_type')

    def create(self, validated_data):
        images_data = validated_data.pop('images', {})
        comment = Comment.objects.create(**validated_data)
        for image_data in images_data.values:
            AttachedImage.objects.create(comment=comment, **image_data)
        return comment
