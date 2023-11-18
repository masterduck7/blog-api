import pytest


@pytest.mark.django_db
class TestBlogArticleModel:
    def test_blog_article_str(self, blog_article):
        assert str(blog_article) == blog_article.title

    def test_blog_article_full_name(self, blog_article):
        assert str(blog_article.full_name()) == blog_article.user.get_full_name()


@pytest.mark.django_db
class TestContactRequestModel:
    def test_contact_request_str(self, contact_request):
        assert str(contact_request) == contact_request.name
