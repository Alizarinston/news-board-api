from rest_framework import serializers
from . import models


class FillAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"author": {"read_only": True}}

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user.username
        return super().create(validated_data)


class PostSerializer(FillAuthorSerializer):
    class Meta(FillAuthorSerializer.Meta):
        model = models.Post
        fields = "__all__"


class CommentSerializer(FillAuthorSerializer):
    class Meta(FillAuthorSerializer.Meta):
        model = models.Comment
        fields = "__all__"
