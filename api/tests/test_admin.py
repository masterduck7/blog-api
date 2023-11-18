import pytest
from django.contrib.admin.sites import AdminSite
from django.urls import reverse

from api.admin import ContactRequestAdmin
from api.models import ContactRequest


@pytest.mark.django_db
class TestContactRequestSuccess:
    def setup_method(self):
        self.url = reverse("api:contact-request-success")

    def test_has_add_permission(self, client, create_super_user):
        contact_request = ContactRequestAdmin(ContactRequest, AdminSite())
        request = client.get("/fake-url/")
        request.user = create_super_user

        has_add_permission = contact_request.has_add_permission(request)
        has_edit_permission = contact_request.has_change_permission(request)
        has_remove_permission = contact_request.has_delete_permission(request)
        assert not has_add_permission
        assert not has_edit_permission
        assert has_remove_permission
