from django.urls import path
from django.views.generic import TemplateView

from api.views.blog_article import BlogArticleList, BlogArticleDetails
from api.views.contact import ContactRequestFormView

app_name = "blog_article"

urlpatterns = [
    path("blog-articles/", BlogArticleList.as_view(), name="blog-article-list"),
    path(
        "blog-articles/<int:pk>/<slug:slug>/",
        BlogArticleDetails.as_view(),
        name="blog-article-details",
    ),
    path("contact-request", ContactRequestFormView.as_view(), name="contact-request"),
    path(
        "contact-request-success/",
        TemplateView.as_view(template_name="contact-request-success.html"),
        name="success",
    ),
]
