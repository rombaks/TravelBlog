from django.views.generic import TemplateView

from rest_framework import viewsets

from .filters import PostFilter, UserFilter
from .models import Post, Tag, User
from .serializers import PostSerializer, TagSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class PostViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    queryset = Post.objects.prefetch_related("author", "tags").order_by("id")
    serializer_class = PostSerializer
    filterset_class = PostFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer


class Home(TemplateView):
    template_name = "home.html"
