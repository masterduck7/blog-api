from rest_framework.pagination import PageNumberPagination
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


class BlogArticleDetails(generics.RetrieveAPIView):
    """
    Get a blog article
    """

    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
