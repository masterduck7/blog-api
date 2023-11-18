from django.contrib import admin

from api.models import BlogArticle, ContactRequest


@admin.register(BlogArticle)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
