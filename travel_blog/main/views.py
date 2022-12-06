from rest_framework import viewsets

from .filters import PostFilter, UserFilter
from .models import Post, Tag, User
from .serializers import PostSerializer, TagSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("author", "tags").order_by("id")
    serializer_class = PostSerializer
    filterset_class = PostFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by("title")
    serializer_class = TagSerializer
