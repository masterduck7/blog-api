import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from api.models import BlogArticle, ContactRequest


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def contact_request():
    contact_request = ContactRequest.objects.create(
        email="test@email.com",
        name="tester",
        content="testing an email",
        date=timezone.now(),
    )
    return contact_request


@pytest.fixture
def create_super_user(db, django_user_model):
    superuser, _ = django_user_model.objects.get_or_create(
        username="admin", password="password", is_staff=True, is_superuser=True
    )

    return superuser


@pytest.fixture
def create_user(db, django_user_model):
    user, _ = django_user_model.objects.get_or_create(
        username="test_user", password="password"
    )

    return user


@pytest.fixture
@pytest.mark.django_db
def blog_article(create_user):
    blog_article = BlogArticle.objects.create(
        title="A new article",
        slug="a-new-article",
        content="A new article content",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )
    return blog_article


@pytest.fixture
@pytest.mark.django_db
def blog_article_big_list(create_user, blog_article):
    article_2 = BlogArticle.objects.create(
        title="A new article 2",
        slug="a-new-article-2",
        content="A new article content 2",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )
    article_3 = BlogArticle.objects.create(
        title="A new article 3",
        slug="a-new-article-3",
        content="A new article content 3",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )
    article_4 = BlogArticle.objects.create(
        title="A new article 4",
        slug="a-new-article-4",
        content="A new article content 4",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )
    article_5 = BlogArticle.objects.create(
        title="A new article 5",
        slug="a-new-article-5",
        content="A new article content 5",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )
    article_6 = BlogArticle.objects.create(
        title="A new article 6",
        slug="a-new-article-6",
        content="A new article content 6",
        publication_datetime=timezone.now(),
        status=True,
        user=create_user,
    )

    return [
        blog_article,
        article_2,
        article_3,
        article_4,
        article_5,
        article_6,
    ]
