from django import forms
from django.core.mail import EmailMessage
from django.conf import settings

from api.models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()

    class Meta:
        model = ContactRequest
        fields = ("email", "name", "content", "date")

    def send_email(self):
        email = EmailMessage(
            subject=f'Contact request from: {self.cleaned_data["name"]}',
            body=self.cleaned_data["content"],
            from_email=self.cleaned_data["email"],
            to=[settings.EMAIL_HOST_USER],
            reply_to=[settings.EMAIL_HOST_USER],
        )

        email.send()
