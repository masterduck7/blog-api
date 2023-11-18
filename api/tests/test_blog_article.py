import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestBlogArticleList:
    def setup_method(self):
        self.blog_article_list = reverse("api:blog-article-list")

    def test_blog_article_list(self, client, blog_article):
        response = client.get(self.blog_article_list)

        assert response.status_code == 200
        assert response.data["total_articles"] == 1
        assert "results" in response.data
        assert response.data["results"][0] == blog_article

    def test_blog_article_list_paginated(self, client, blog_article_big_list):
        response = client.get(self.blog_article_list)

        assert response.status_code == 200
        assert response.data["current_page"] == 1
        assert response.data["total_pages"] == 2
        assert response.data["total_articles"] == 6
        assert "results" in response.data
        for result in response.data["results"]:
            result in blog_article_big_list


@pytest.mark.django_db
class TestBlogArticleDetails:
    def test_blog_article_details(self, client, blog_article):
        url = reverse(
            "api:blog-article-details",
            kwargs={"slug": blog_article.slug, "pk": blog_article.pk},
        )
        response = client.get(url)

        assert response.status_code == 200
        assert response.data["blog_article"] == blog_article
