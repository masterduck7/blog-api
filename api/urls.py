from django.urls import path

from api.views.blog_article import BlogArticleList, BlogArticleDetails

app_name = "blog_article"

urlpatterns = [
    path("blog-articles/", BlogArticleList.as_view(), name="blog-article-list"),
    path(
        "blog-articles/<int:pk>",
        BlogArticleDetails.as_view(),
        name="blog-article-details",
    ),
]
