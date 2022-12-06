from rest_framework import serializers

from .models import post, tag, user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = ("id", "username", "first_name", "last_name", "email")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag.Tag
        fields = (
            "id",
            "title",
        )


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = post.Post
        fields = (
            "id",
            "title",
            "slug",
            "author",
            "created_at",
            "updated_at",
            "status",
            "content",
            "tags",
        )
