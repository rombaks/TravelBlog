from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Tag, User


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "status",
    )
    list_display_links = (
        "title",
        "author",
    )
    search_fields = ("title",)


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, admin.ModelAdmin)
