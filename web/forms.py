from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": widgets.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "subject": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "message": widgets.Textarea(attrs={"class": "form-control","placeholder": "Write your message",})
        }