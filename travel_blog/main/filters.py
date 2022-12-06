import django_filters

from .models import Post, User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "last_name": ["icontains"],
        }


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {"title": ["iexact"]}
