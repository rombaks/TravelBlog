from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField

from .tag import Tag
from .user import User


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from="title")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag, related_name="post_tags", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
