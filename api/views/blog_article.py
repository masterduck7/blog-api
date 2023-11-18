from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics

from api.models import BlogArticle
from api.serializers.blog_article import BlogArticleSerializer


class BlogArticlePagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "total_articles": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "page_range": self.page.paginator.page_range,
                "results": data,
            }
        )


class BlogArticleList(generics.ListAPIView):
    """
    Get entries paginated by 5 items
    """

    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    pagination_class = BlogArticlePagination
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = "blog_article_list.html"

    def get(self, request):
        paginate_queryset = self.paginate_queryset(self.get_queryset())
        return self.get_paginated_response(paginate_queryset)


class BlogArticleDetails(generics.RetrieveAPIView):
    """
    Get a blog article
    """

    def get_object(self):
        return BlogArticle.objects.get(
            pk=self.kwargs["pk"],
            slug=self.kwargs["slug"],
        )

    serializer_class = BlogArticleSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response(
            {"blog_article": self.object}, template_name="blog_article_details.html"
        )
