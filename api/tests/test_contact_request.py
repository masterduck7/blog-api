import pytest
from pytest_django.asserts import assertTemplateUsed
from datetime import datetime
from django.urls import reverse
from django.utils import timezone

from api.models import ContactRequest


@pytest.mark.django_db
class TestContactRequestSuccess:
    def setup_method(self):
        self.url = reverse("api:contact-request-success")

    def test_contact_request(self, client):
        response = client.get(self.url)

        assert response.status_code == 200
        assertTemplateUsed(response, "contact_request_success.html")


@pytest.mark.django_db
class TestContactRequest:
    def setup_method(self):
        self.data = {
            "email": "test_email@email.com",
            "name": "test_name",
            "content": "test_content",
            "date": datetime.strftime(timezone.now(), "%Y-%m-%d"),
        }
        self.url = reverse("api:contact-request")

    def test_contact_request(self, client):
        response = client.post(self.url, data=self.data)
        contact_request = ContactRequest.objects.get(name=self.data["name"])

        assert response.status_code == 302
        assert contact_request
        assert contact_request.email == self.data["email"]
