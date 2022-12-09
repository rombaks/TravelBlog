import django_filters

from .models import Post, User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "username": ["icontains"],
        }


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {"title": ["icontains"]}
