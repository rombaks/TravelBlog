from django.contrib import admin
from django.urls import include, path, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .main.views import Home, PostViewSet, TagViewSet, UserViewSet


router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"tags", TagViewSet, basename="tags")

schema_view = get_schema_view(
    openapi.Info(
        title="Travel blog API",
        default_version="v1",
        description="A travel blog written with Django",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rombaks.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/", include(router.urls)),
    path("", Home.as_view(), name="home"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

admin.site.site_header = "Travel blog"
admin.site.site_title = "rombaks"
admin.site.index_title = "Travel blog"
