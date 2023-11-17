from django.contrib import admin

from api.models import Blog, ContactRequest


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }


admin.site.register(ContactRequest)
