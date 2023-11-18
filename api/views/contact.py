from django.views.generic.edit import FormView

from api.forms import ContactRequestForm
from api.models import ContactRequest


class ContactRequestFormView(FormView):
    template_name = "contact_request.html"
    form_class = ContactRequestForm
    success_url = "/contact-request-success/"

    def form_valid(self, form):
        ContactRequest.objects.create(
            email=form.cleaned_data["email"],
            name=form.cleaned_data["name"],
            content=form.cleaned_data["content"],
            date=form.cleaned_data["date"],
        )
        form.send_email()
        return super().form_valid(form)
