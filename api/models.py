from django.contrib.auth.models import User
from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.CharField(max_length=200, blank=False, null=False)
    publication_datetime = models.DateTimeField(blank=False, null=False)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(
        User,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="user",
    )

    def __str__(self):
        return self.title

    def full_name(self):
        return self.user.get_full_name()


class ContactRequest(models.Model):
    email = models.CharField(max_length=200, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name
